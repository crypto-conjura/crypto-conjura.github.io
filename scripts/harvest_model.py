#!/usr/bin/env python3
"""Model plumbing for scripts/harvest_conjectures.py.

Two things live here and nothing else: the JSON schemas the three model calls
are constrained to, and the two backends that can serve those calls. The
harvest pipeline itself -- what gets asked, in what order, and which answers
are believed -- is in `harvest_conjectures.py`, and the wording of the asks is
in `prompts/harvest.md`.

Backends
--------

`api`  The Anthropic SDK (`pip install anthropic`). The PDF is sent as a
       native `document` block, so the model sees the *rendered* pages --
       displayed equations, figures, the boxed theorem environments that
       carry the conjectures -- rather than a text layer with the mathematics
       flattened out of it. This is the higher-fidelity path and the one to
       prefer for a mathematics paper. Needs credentials: ANTHROPIC_API_KEY,
       or an `ant auth login` profile.

`cli`  The Claude Code CLI (`claude -p`), which is already authenticated on a
       machine where Claude Code runs and therefore needs no API key. Here the
       PDF is not inlined; the model is given its path and reads it with the
       Read tool, which renders pages as images twenty at a time, so a long
       paper is read in several passes within the one agent turn.

Both are constrained to a JSON Schema -- `output_config.format` on the API,
`--json-schema` on the CLI -- so neither can return prose where the pipeline
expects a record. Validation happens at the tool-call layer, which means a
mismatch is retried by the model rather than crashing the run.

`pick_backend()` chooses: `api` when the SDK is importable and credentials
are visible, `cli` otherwise. Override with `--backend`.
"""

from __future__ import annotations

import base64
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

MODEL_API = "claude-opus-5"
MODEL_CLI = "opus"

# Server-side refusal fallback. Claude Opus 5 runs safety classifiers that can
# decline a request outright (HTTP 200, stop_reason "refusal"); cryptanalysis
# sits close enough to the cyber category that a benign paper occasionally
# trips one. With this on, the API re-runs the declined request on Anthropic's
# recommended fallback inside the same call instead of handing back a refusal.
# Dropped automatically if the account cannot use the beta -- see _stream_api.
FALLBACK_BETA = "server-side-fallback-2026-07-01"

# Request ceilings the Messages API enforces on an inlined PDF.
MAX_PDF_BYTES = 30 * 1024 * 1024      # 32MB request cap, less room for the prompt
MAX_PDF_PAGES = 600


# --------------------------------------------------------------------------
# Schemas
#
# Structured outputs accept a subset of JSON Schema: no recursion, no
# numeric or string constraints, no minItems, and every object needs
# `additionalProperties: false` plus a `required` listing every property.
# Counts and lengths are therefore checked in Python, not here. Nothing is
# optional at the schema level either -- "none" is the empty string or the
# empty array, so the model can never omit a field it found inconvenient.
# --------------------------------------------------------------------------

def _obj(props, **kw):
    return {
        "type": "object",
        "additionalProperties": False,
        "required": sorted(props),
        "properties": props,
        **kw,
    }


_QUOTE = _obj({
    "page": {
        "type": "integer",
        "description": "1-based page of the PDF this text is printed on.",
    },
    "role": {
        "type": "string",
        "enum": ["statement", "openness", "definition", "parameter", "progress"],
        "description": "What this quote is evidence *for*.",
    },
    "text": {
        "type": "string",
        "description": (
            "Verbatim prose from the paper, copied character for character, "
            "one to three sentences. Prefer spans that are mostly words: this "
            "string is checked mechanically against the PDF's text layer, and "
            "heavy mathematics does not survive extraction intact."
        ),
    },
})

_CANDIDATE = _obj({
    "slug": {
        "type": "string",
        "description": "Lowercase kebab-case folder name, two to four words, e.g. split-decomp.",
    },
    "title": {"type": "string", "description": "Title case, no trailing period."},
    "subtitle": {"type": "string", "description": "One clause naming the regime, or empty."},
    "category": {
        "type": "string",
        "description": "Site category, e.g. 'Idealized Models & Non-Uniformity'.",
    },
    "one_line": {
        "type": "string",
        "description": "One sentence, plain English, no LaTeX. What is being conjectured.",
    },
    "informal": {
        "type": "string",
        "description": (
            "One paragraph of plain English for the informalconjecture box. "
            "No numbered references, no undefined symbols, no LaTeX beyond "
            "inline $...$ for a bare parameter name."
        ),
    },
    "setting_latex": {
        "type": "string",
        "description": (
            "LaTeX prose for the 'setting' section: where the problem comes "
            "from, why it matters, what is already known. Cite with "
            "\\cite{Key} against the bibliography array."
        ),
    },
    "notation_latex": {
        "type": "string",
        "description": (
            "LaTeX defining every symbol the formal statement uses, and "
            "nothing it does not use."
        ),
    },
    "definitions_latex": {
        "type": "string",
        "description": (
            "Zero or more complete \\begin{definition}...\\end{definition} "
            "blocks the conjecture depends on, or empty."
        ),
    },
    "formal_statement_latex": {
        "type": "string",
        "description": (
            "The body of a single \\begin{conjecture}...\\end{conjecture} "
            "(without the surrounding environment). Self-contained against "
            "notation_latex and definitions_latex. Quantifiers and parameter "
            "ranges explicit."
        ),
    },
    "parameters": {
        "type": "array",
        "items": _obj({
            "symbol": {"type": "string"},
            "meaning": {"type": "string"},
        }),
    },
    "status_note": {
        "type": "string",
        "description": "One or two sentences: exactly which cases are settled and which are open.",
    },
    "progress_note": {
        "type": "string",
        "description": "What partial results the paper reports towards this, or empty.",
    },
    "openness_kind": {
        "type": "string",
        "enum": [
            "paper-states-open",
            "paper-conjectures",
            "paper-asks-question",
            "paper-notes-technique-fails",
        ],
        "description": (
            "How the paper leaves it open. There is deliberately no value for "
            "'the reader could ask this' -- if the paper does not leave it "
            "open, it is not a candidate."
        ),
    },
    "quotes": {
        "type": "array",
        "items": _QUOTE,
        "description": (
            "At least three: one whose role is 'statement', one whose role is "
            "'openness', and at least one more."
        ),
    },
    "pages": {
        "type": "array",
        "items": {"type": "integer"},
        "description": "Every PDF page this conjecture was read off.",
    },
    "bibliography": {
        "type": "array",
        "items": _obj({
            "key": {"type": "string", "description": "\\bibitem key, e.g. CDGS."},
            "authors": {"type": "string"},
            "title": {"type": "string"},
            "venue": {"type": "string"},
            "year": {"type": "string"},
            "verified": {
                "type": "string",
                "enum": ["printed-in-source-bibliography", "unverified"],
                "description": (
                    "'printed-in-source-bibliography' only if you read this "
                    "entry in the harvested PDF's own reference list. Anything "
                    "recalled from memory is 'unverified' and will be marked "
                    "as such in the output."
                ),
            },
        }),
    },
    "why_interesting": {"type": "string"},
    "why_clean": {"type": "string"},
    "risks": {
        "type": "string",
        "description": "What a reviewer should check hardest, or where you are least sure.",
    },
})

EXTRACT_SCHEMA = _obj({
    "document": _obj({
        "title": {"type": "string"},
        "authors": {"type": "array", "items": {"type": "string"}},
        "venue_or_archive": {"type": "string"},
        "year": {"type": "string"},
        "identifier": {"type": "string", "description": "DOI, ePrint number, arXiv id, or empty."},
        "citation_confidence": {
            "type": "string",
            "enum": ["printed-on-page", "inferred", "unknown"],
        },
    }),
    "candidates": {"type": "array", "items": _CANDIDATE},
    "rejected": {
        "type": "array",
        "items": _obj({
            "what": {"type": "string"},
            "why": {"type": "string"},
        }),
        "description": (
            "Open questions in the paper you looked at and did not promote, "
            "with the reason. A reviewer needs to see what was passed over."
        ),
    },
})

VERIFY_SCHEMA = _obj({
    "verdict": {
        "type": "string",
        "enum": [
            "faithful",
            "faithful-with-corrections",
            "unfaithful",
            "not-a-conjecture",
        ],
    },
    "confidence": {"type": "string", "enum": ["high", "medium", "low"]},
    "checks": {
        "type": "array",
        "items": _obj({
            "name": {"type": "string"},
            "result": {"type": "string", "enum": ["pass", "fail", "unclear"]},
            "page": {"type": "integer", "description": "Page the evidence is on, or 0."},
            "finding": {"type": "string"},
        }),
    },
    "fabrications": {
        "type": "array",
        "items": {"type": "string"},
        "description": "Anything asserted in the draft that the paper does not support.",
    },
    "corrections": {
        "type": "array",
        "items": _obj({
            "field": {"type": "string"},
            "problem": {"type": "string"},
            "corrected": {"type": "string"},
        }),
    },
    "reason": {"type": "string", "description": "Two or three sentences for the verdict."},
})

TEX_SCHEMA = _obj({
    "runninghead": {"type": "string", "description": "SHORT TITLE IN CAPS."},
    "tex": {
        "type": "string",
        "description": "The complete statement.tex, \\documentclass to \\end{document}.",
    },
    "notes": {"type": "string", "description": "Anything a reviewer should know, or empty."},
})


class ModelError(RuntimeError):
    """A model call failed in a way the pipeline should record, not crash on."""


class Refusal(ModelError):
    """Safety classifiers declined the request."""


# --------------------------------------------------------------------------
# Backends
# --------------------------------------------------------------------------

class Backend:
    name = "abstract"

    def complete(self, *, system, prompt, schema, pdf, max_tokens, effort, label):
        """Return the parsed object the schema describes.

        `pdf` is a PdfDoc, or None for a call that has no business consulting
        the paper -- typesetting an already-checked record is the case, and
        withholding the source there is a feature, not an economy.
        """
        raise NotImplementedError


class AnthropicBackend(Backend):
    name = "api"

    def __init__(self, model=MODEL_API, use_fallbacks=True, text_only=False):
        import anthropic  # deferred: the CLI backend must work without it

        self.anthropic = anthropic
        self.client = anthropic.Anthropic()
        self.model = model
        self.use_fallbacks = use_fallbacks
        self.text_only = text_only
        self._b64 = {}

    def _document_block(self, pdf):
        if self.text_only:
            return {
                "type": "text",
                "text": (
                    "The paper's extracted text layer follows. Mathematics is "
                    "flattened by the extractor and page breaks are marked "
                    "with [[page N]].\n\n" + pdf.marked_text()
                ),
                "cache_control": {"type": "ephemeral"},
            }
        if pdf.path not in self._b64:
            if pdf.size > MAX_PDF_BYTES:
                raise ModelError(
                    f"{pdf.path.name} is {pdf.size / 1e6:.1f}MB; the API caps a request "
                    f"at 32MB. Re-run with --text-only for this file."
                )
            if pdf.pages > MAX_PDF_PAGES:
                raise ModelError(
                    f"{pdf.path.name} has {pdf.pages} pages; the API caps a PDF at "
                    f"{MAX_PDF_PAGES}. Re-run with --text-only for this file."
                )
            self._b64[pdf.path] = base64.standard_b64encode(pdf.path.read_bytes()).decode()
        return {
            "type": "document",
            "source": {
                "type": "base64",
                "media_type": "application/pdf",
                "data": self._b64[pdf.path],
            },
            "title": pdf.path.name,
            # The PDF is the expensive, unchanging prefix of all three calls
            # against this paper; a breakpoint here makes calls two and three
            # cache reads rather than full re-uploads.
            "cache_control": {"type": "ephemeral"},
        }

    def complete(self, *, system, prompt, schema, pdf, max_tokens, effort, label):
        content = [{"type": "text", "text": prompt}]
        if pdf is not None:
            content.insert(0, self._document_block(pdf))
        kw = dict(
            model=self.model,
            max_tokens=max_tokens,
            system=[{"type": "text", "text": system}],
            thinking={"type": "adaptive"},
            output_config={
                "effort": effort,
                "format": {"type": "json_schema", "schema": schema},
            },
            messages=[{"role": "user", "content": content}],
        )
        msg = self._stream(kw)
        if msg.stop_reason == "refusal":
            cat = getattr(getattr(msg, "stop_details", None), "category", None)
            raise Refusal(f"{label}: request declined (category: {cat or 'unspecified'})")
        if msg.stop_reason == "max_tokens":
            raise ModelError(f"{label}: hit max_tokens ({max_tokens}); output is truncated")
        text = next((b.text for b in msg.content if b.type == "text"), "")
        try:
            return json.loads(text)
        except json.JSONDecodeError as exc:
            raise ModelError(f"{label}: response was not JSON ({exc})") from exc

    def _stream(self, kw):
        """Stream the request, dropping the fallback beta if it is unavailable.

        Streaming is not optional at these max_tokens: a non-streaming request
        the SDK estimates will run past ten minutes is refused outright, and a
        thorough read of a forty-page paper at high effort is exactly that.
        """
        if self.use_fallbacks:
            try:
                with self.client.beta.messages.stream(
                    betas=[FALLBACK_BETA], fallbacks="default", **kw
                ) as stream:
                    return stream.get_final_message()
            except self.anthropic.BadRequestError as exc:
                if "fallback" not in str(exc).lower():
                    raise
                # Account or route cannot use the beta. Note it once and carry
                # on without the safety net rather than failing the harvest.
                print(
                    "  ! server-side refusal fallback unavailable; continuing without it",
                    file=sys.stderr,
                )
                self.use_fallbacks = False
        with self.client.messages.stream(**kw) as stream:
            return stream.get_final_message()


class ClaudeCliBackend(Backend):
    name = "cli"

    def __init__(self, model=MODEL_CLI, binary="claude", budget_usd=None, text_only=False):
        self.model = model
        self.binary = binary
        self.budget_usd = budget_usd
        self.text_only = text_only

    def complete(self, *, system, prompt, schema, pdf, max_tokens, effort, label):
        tools = []
        if pdf is None:
            body = prompt
        elif self.text_only:
            body = (
                f"{prompt}\n\n---\n\nThe paper's extracted text layer follows. "
                f"Mathematics is flattened by the extractor and page breaks are "
                f"marked with [[page N]].\n\n{pdf.marked_text()}"
            )
        else:
            body = (
                f"{prompt}\n\n---\n\nThe paper is the PDF at `{pdf.path}` "
                f"({pdf.pages} pages). Read it with the Read tool, which takes at "
                f"most twenty pages per call, so work through it in ranges "
                f'(pages: "1-20", "21-40", ...) until you have seen every page '
                f"that matters. `pdftotext -layout -f N -l N {pdf.path} -` gives you "
                f"the text layer of page N if you need to copy a quote exactly."
            )
            tools = ["Read", "Bash(pdftotext:*)"]

        cmd = [
            self.binary, "-p", body,
            "--model", self.model,
            "--effort", effort,
            "--output-format", "json",
            "--json-schema", json.dumps(schema),
            "--append-system-prompt", system,
            "--no-session-persistence",
        ]
        if tools:
            cmd += ["--allowed-tools", *tools, "--add-dir", str(pdf.path.parent)]
        if self.budget_usd:
            cmd += ["--max-budget-usd", str(self.budget_usd)]

        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode != 0:
            tail = (proc.stderr or proc.stdout or "").strip()[-800:]
            raise ModelError(f"{label}: claude exited {proc.returncode}: {tail}")
        try:
            env = json.loads(proc.stdout)
        except json.JSONDecodeError as exc:
            raise ModelError(f"{label}: claude did not return JSON ({exc})") from exc
        if env.get("is_error") or env.get("subtype") not in (None, "success"):
            raise ModelError(f"{label}: {env.get('subtype')}: {str(env.get('result'))[:400]}")
        # `structured_output` is the schema-validated object; `result` is the
        # same thing as a string. Prefer the former where the CLI supplies it.
        result = env.get("structured_output")
        if result is None:
            result = env.get("result")
        if isinstance(result, (dict, list)):
            return result
        try:
            return json.loads(result)
        except (json.JSONDecodeError, TypeError) as exc:
            raise ModelError(f"{label}: result was not the requested JSON ({exc})") from exc


def credentials_visible():
    """Whether the SDK would find something to authenticate with."""
    if os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("ANTHROPIC_AUTH_TOKEN"):
        return True
    cfg = Path(os.environ.get("ANTHROPIC_CONFIG_DIR", Path.home() / ".config" / "anthropic"))
    return (cfg / "credentials").is_dir() and any((cfg / "credentials").glob("*.json"))


def pick_backend(choice, *, budget_usd=None, text_only=False):
    """Resolve `--backend auto|api|cli` to an instance, explaining a failure."""
    have_sdk = True
    try:
        import anthropic  # noqa: F401
    except ImportError:
        have_sdk = False
    have_cli = shutil.which("claude") is not None

    if choice == "api" or (choice == "auto" and have_sdk and credentials_visible()):
        if not have_sdk:
            raise SystemExit(
                "The api backend needs the Anthropic SDK: pip install anthropic\n"
                "Or use --backend cli, which goes through the Claude Code CLI."
            )
        return AnthropicBackend(text_only=text_only)

    if choice in ("cli", "auto"):
        if not have_cli:
            raise SystemExit(
                "No backend available. Either install the Anthropic SDK and set\n"
                "ANTHROPIC_API_KEY (--backend api), or install the Claude Code CLI\n"
                "(--backend cli). See scripts/harvest_model.py for the difference."
            )
        return ClaudeCliBackend(budget_usd=budget_usd, text_only=text_only)

    raise SystemExit(f"unknown backend: {choice}")
