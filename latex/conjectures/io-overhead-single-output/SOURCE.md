# Provenance: Obfuscation Overhead for Single-Output Circuits

Written in-session following `prompts/harvest.md`; `scripts/harvest_conjectures.py`
could not run its model stage on this machine. Nothing here was checked by a
human yet; this file is what the run believed and why.

## Source

- Paper: **Lower Bounds on the Overhead of Indistinguishability Obfuscation**
- Authors: Zhenjian Lu, Noam Mazor, Igor C. Oliveira, Rafael Pass
- Venue/archive: IACR ePrint 2024
- Identifier: IACR ePrint 2024/1524
- Bibliographic detail: inferred
- File: `2024-1524.pdf` (50 pages)
- sha256: `63ab8ac34c39c243938693ec98fb3f4e5eaa2967df0aa8e2169cbe68b2de7500`
- Read on 2026-08-28T02:30:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and this file are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-states-open`. The first of the source's named main open problems. Its main theorem gives an Omega(s/log s) additive overhead lower bound for multi-output circuits under NP not in BPP, an assumption that is minimal since a zero-overhead iO scheme exists if NP is in BPP. The single-output case is not covered.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. Where `found` differs from the claimed page, the claim was
wrong and the found page is what the statement cites.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 12 | 12 | exact (100%) | As our main open problems, we leave the extension of our (database-free) impossibility results to the setting of single-output circuits, the investigation of iO |
| notknown | 5 | 5 | exact (100%) | we currently do not know how to establish them for single-output Boolean circuits nor for multi-output circuits where we allow unbounded fan-in gates when measu |
| obstruction | 8 | 8 | exact (100%) | This remains a challenging open problem, and can be seen as an important step towards establishing the NP-hardness of MCSP for single-output Boolean functions. |
| padding | 8 | 8 | exact (100%) | This allows us to establish thorough a simple padding argument that the hardness of iO for arbitrary multi-output circuits |
| bottleneck | 33 | 33 | exact (100%) | The choice of parameters governing this gap are constrained by the encoding argument presented near the end of the proof, which does not seem to allow an additi |
| minimal | 1 | 1 | exact (100%) | The hardness assumption under which this negative result holds is minimal since an optimal iO scheme with no circuit size overhead exists if NP ⊆ BPP. |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The source names the direction without restating the bound, so the specific form -- same s + o(s/log s) target, same NP not in BPP assumption -- is this statement's choice and is flagged as such. Four page claims were corrected by grounding: the single-output remark is on page 5 not 8, the MCSP obstruction and the padding argument on page 8 not 9, and the bottleneck remark on page 33 not 32. The statement separates two things easy to conflate: the padding from arbitrary multi-output shapes to the square case is solved, while the drop to one output bit is not.

## Build

`pdflatex` clean; `chktex -q` 0 warnings under the per-folder `.chktexrc`
(every suppression documented in that file, checked hit by hit);
`lacheck` silent.
