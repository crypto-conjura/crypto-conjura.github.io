#!/usr/bin/env python3
"""Generates the StackExchange-style topic-tag pages from each c/*/index.qmd's
`topics:` frontmatter field (validated and enumerated in build_index.py's
TOPIC_SLUGS).

Three things are generated, all from the same data, none of them hand-edited:

  - problems/by-topic/<slug>/index.qmd   one listing page per topic in use,
    a short tag-wiki paragraph followed by a Quarto `listing:` block over
    the matching _generated/topics/<slug>.yml (written by build_index.py --
    run that first).
  - problems/by-topic/index.qmd          the browse-all overview: every topic
    in use, sized by how many statements carry it, sorted by that count.
  - the managed `<!-- topics:start -->...<!-- topics:end -->` block in every
    c/*/index.qmd body, right after the existing status-badge block: clickable
    chips for that page's own topics, so a reader doesn't have to leave the
    statement to see what it's about.

    python3 scripts/gen_topics.py           # write everything
    python3 scripts/gen_topics.py --check   # report drift, exit 1 if any, write nothing

Run scripts/build_index.py first (or as part of the same commit): this script
reads TOPIC_SLUGS from it and expects _generated/topics/<slug>.yml to already
be current for the listing pages it (re)writes.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_index import ROOT, STATEMENTS_DIR, TOPIC_SLUGS, load_frontmatter  # noqa: E402

BY_TOPIC_DIR = ROOT / "problems" / "by-topic"

# One paragraph each: the tag-wiki text a reader sees at the top of the
# topic's own listing page. Kept here, not in build_index.py, since only page
# generation needs the prose -- the schema only needs the slug.
TOPIC_DESCRIPTIONS = {
    "feistel-networks": "Constructions built from the Feistel round structure, and how many rounds are needed for indifferentiability or indistinguishability from a random permutation.",
    "pseudorandom-permutations": "Block-cipher-style constructions analyzed as permutations that should be indistinguishable from a uniformly random one.",
    "mirror-theory": "The mirror-theory (H-coefficient) counting technique for bounding the security of block-cipher-based modes.",
    "block-ciphers": "Statements about the internal structure or security of a specific block cipher construction.",
    "indifferentiability": "The indifferentiability framework for showing an idealized construction is as good as the random object it is meant to instantiate.",
    "collision-finding": "Time, query, and memory complexity of finding collisions -- including k-way and other structured collisions -- in a random function or permutation.",
    "time-space-tradeoffs": "Tradeoffs between offline precomputation and online query time for a cryptanalytic search task.",
    "limited-independence": "What t-wise (limited) independence of a distribution does, and does not, imply.",
    "leftover-hash-lemma": "The leftover hash lemma and the tightness of its randomness-extraction bound.",
    "randomness-extraction": "Extracting near-uniform randomness from a weak or structured source.",
    "multi-source-extractors": "Extraction from several independent, non-communicating weak sources.",
    "random-oracle-model": "Statements set in the classical (non-quantum) random oracle model.",
    "quantum-random-oracle-model": "Statements set in the quantum random oracle model, where the oracle may be queried in superposition.",
    "generic-group-model": "Statements set in a generic group model (Shoup's or Maurer's), where the adversary accesses group operations only through an oracle.",
    "compressed-oracle": "Zhandry's compressed-oracle method for tracking a quantum algorithm's queries to a random function or permutation.",
    "black-box-separations": "Impossibility or separation results ruling out a fully black-box construction or reduction between two primitives.",
    "one-way-functions": "The minimal cryptographic assumption, and what it does or does not imply in a black-box sense.",
    "collision-resistant-hashing": "Collision-resistant hash functions as a primitive, and their relations to other assumptions.",
    "snarks": "Succinct non-interactive arguments of knowledge, and the proof systems and linear-proof abstractions behind them.",
    "proof-size-lower-bounds": "Lower bounds on how small a non-interactive argument or proof can be.",
    "non-interactive-key-exchange": "Multi-party key exchange with no interaction, typically analyzed in a generic group model.",
    "key-agreement": "Two-party protocols for agreeing on a shared secret, and their black-box (im)possibility from weaker primitives.",
    "blind-signatures": "Signature schemes that let a signer sign a message without seeing it, and round-complexity lower bounds for them.",
    "signature-schemes": "Digital signature constructions and the tightness of their security reductions.",
    "threshold-signatures": "Signature schemes distributed across multiple signers under a corruption threshold.",
    "tight-reductions": "Security reductions whose loss is a constant rather than growing with the adversary's resources.",
    "learning-with-errors": "Ring- or Module-LWE-specific hardness questions.",
    "quantum-query-complexity": "Upper and lower bounds on the number of quantum queries needed against an oracle-based primitive.",
    "quantum-cryptography": "General security notions, constructions, and separations involving quantum adversaries or quantum information.",
    "quantum-key-agreement": "Key-agreement protocols and attacks in a setting with quantum parties or quantum queries.",
    "sum-of-squares": "The sum-of-squares semidefinite-programming hierarchy, and its use for rounding algorithms and hardness arguments.",
    "log-rank-conjecture": "The log-rank conjecture in communication complexity, and statements closely related to it.",
    "quantum-information": "Entanglement, separability, and other problems studied within quantum information theory.",
    "verifiable-delay-functions": "Functions that take a prescribed amount of sequential time to evaluate but are quickly verifiable, and their (un)computational uniqueness.",
    "time-lock-puzzles": "Puzzles that hide a value for a controlled, only sequentially reducible, amount of time.",
    "byzantine-agreement": "Consensus protocols tolerating malicious parties, and their resilience bounds.",
    "coin-tossing": "Fair coin-flipping protocols and the bias an adversary can force, following Cleve's impossibility result.",
    "fine-grained-cryptography": "Cryptographic constructions based on worst-case, fine-grained hardness assumptions rather than average-case ones.",
    "registration-based-encryption": "Encryption schemes that remove the trusted key-generation authority of identity-based encryption in favour of a public registration process.",
    "commitment-schemes": "Commitment protocols and their binding and hiding properties, including in composable or setup-free settings.",
    "physically-uncloneable-functions": "Protocols built from hardware tokens whose physical structure cannot be efficiently cloned.",
    "pseudorandom-generators": "Constructions stretching a short seed into a longer pseudorandom string, and their algebraic structure.",
    "planted-constraint-satisfaction": "Average-case hardness of recovering a planted solution to a random constraint-satisfaction instance, such as planted k-XOR.",
    "average-case-hardness": "Hardness of a computational problem on a natural random input distribution, as opposed to worst-case hardness.",
    "expander-graphs": "Expansion properties of random or structured graphs, and how to certify them.",
    "garbled-circuits": "Yao's garbling technique for two-party computation, and constructions or separations built from it.",
    "witness-encryption": "Encryption schemes where decryption is possible given a witness to an NP statement.",
    "one-shot-signatures": "Quantum signature-like primitives that can be used at most once, related to no-cloning.",
    "search-trees": "Optimal construction of search trees over structured query distributions.",
    "direct-product-theorems": "Theorems on whether solving many independent instances of a hard problem is proportionally harder than solving one.",
    "quantum-encryption-notions": "Relations among competing definitions of IND-CPA-style security against quantum adversaries.",
}

missing_desc = TOPIC_SLUGS - set(TOPIC_DESCRIPTIONS)
if missing_desc:
    raise SystemExit(f"TOPIC_DESCRIPTIONS is missing: {sorted(missing_desc)}")
extra_desc = set(TOPIC_DESCRIPTIONS) - TOPIC_SLUGS
if extra_desc:
    raise SystemExit(f"TOPIC_DESCRIPTIONS has stale entries not in TOPIC_SLUGS: {sorted(extra_desc)}")


def humanize(slug):
    """black-box-separations -> Black Box Separations. Deliberately the same,
    simple, no-small-words-exception transform used in the .ejs.md listing
    template (in JS there) and here (in Python), so a chip reads identically
    whether it was rendered by Quarto's listing engine or written directly
    into a statement page's body -- consistency across the two renderers
    matters more than shaving one preposition's capital letter."""
    return " ".join(w[:1].upper() + w[1:] for w in slug.split("-") if w)


def topic_page(slug):
    label = humanize(slug)
    desc = TOPIC_DESCRIPTIONS[slug]
    return f"""---
title: "{label}"
listing:
  id: topic-{slug}
  contents: "../../../_generated/topics/{slug}.yml"
  type: table
  template: "../../../_listing-templates/statement-table.ejs.md"
  sort: [title]
  sort-ui: false
  page-size: 15
---

{desc}
"""


def overview_page(counts):
    # Sorted by count desc then slug asc, the StackExchange /tags convention.
    # Font size scaled linearly between the least- and most-used topic so the
    # cloud actually reads as a cloud rather than a uniform list; with a
    # single distinct count in play (unlikely once the taxonomy grows) every
    # chip gets the same, still-legible size.
    ordered = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    lo = min(counts.values())
    hi = max(counts.values())
    span = hi - lo or 1
    lines = []
    for slug, n in ordered:
        size = 0.85 + 0.85 * (n - lo) / span
        lines.append(
            f'<a class="cj-tag-cloud-item" href="/problems/by-topic/{slug}/" '
            f'style="font-size: {size:.2f}em;">{humanize(slug)} '
            f'<span class="cj-tag-count">{n}</span></a>'
        )
    body = "\n".join(lines)
    return f"""---
title: "By Topic"
aliases:
  - /problems/tags/index.qmd
---

Every statement carries several fine-grained topic tags, StackExchange-style, in addition to its broad [area](/problems/by-area/index.qmd). Click a tag to see every statement carrying it; size is scaled by how many statements do.

::: {{.cj-tag-cloud}}
{body}
:::
"""


TOPICS_BLOCK_RE = re.compile(
    r"<!-- topics:start -->\n.*?<!-- topics:end -->\n?", re.DOTALL
)
STATUS_END_RE = re.compile(r"(<!-- status:end -->\n)")


def topics_block(topics):
    chips = "".join(
        f'<a class="cj-tag cj-tag-topic" href="/problems/by-topic/{tp}/">{humanize(tp)}</a>'
        for tp in sorted(topics)
    )
    return f'<!-- topics:start -->\n<div class="cj-tags cj-page-topics">{chips}</div>\n<!-- topics:end -->\n'


def update_page_chips(path, fm):
    text = path.read_text(encoding="utf-8")
    new_block = topics_block(fm.get("topics") or [])
    if TOPICS_BLOCK_RE.search(text):
        new_text = TOPICS_BLOCK_RE.sub(new_block, text, count=1)
    elif STATUS_END_RE.search(text):
        new_text = STATUS_END_RE.sub(r"\1\n" + new_block, text, count=1)
    else:
        raise ValueError(f"{path}: no <!-- status:end --> marker to anchor the topics block after")
    changed = new_text != text
    if changed:
        path.write_text(new_text, encoding="utf-8")
    return changed


def run(check):
    leaves = {}
    for path in sorted(STATEMENTS_DIR.glob("*/index.qmd")):
        fm = load_frontmatter(path)
        leaves[path] = fm

    counts = {}
    for fm in leaves.values():
        for tp in fm.get("topics") or []:
            counts[tp] = counts.get(tp, 0) + 1

    unknown = set(counts) - TOPIC_SLUGS
    if unknown:
        print(f"ERROR: topics in use but not in TOPIC_SLUGS: {sorted(unknown)}", file=sys.stderr)
        return 1

    changed = []
    stale = []

    for slug in sorted(counts):
        path = BY_TOPIC_DIR / slug / "index.qmd"
        content = topic_page(slug)
        if not path.exists() or path.read_text(encoding="utf-8") != content:
            stale.append(str(path.relative_to(ROOT)))
            if not check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")
                changed.append(path)

    overview_path = BY_TOPIC_DIR / "index.qmd"
    overview_content = overview_page(counts)
    if not overview_path.exists() or overview_path.read_text(encoding="utf-8") != overview_content:
        stale.append(str(overview_path.relative_to(ROOT)))
        if not check:
            overview_path.write_text(overview_content, encoding="utf-8")
            changed.append(overview_path)

    for path, fm in leaves.items():
        if check:
            text = path.read_text(encoding="utf-8")
            new_block = topics_block(fm.get("topics") or [])
            current = TOPICS_BLOCK_RE.search(text)
            if not current or current.group(0) != new_block:
                stale.append(str(path.relative_to(ROOT)))
        else:
            if update_page_chips(path, fm):
                changed.append(path)

    # Orphan topic pages: a slug that used to have statements and no longer
    # does. Reported, not deleted -- silently removing a page a reader may
    # have bookmarked is a bigger mistake than leaving a stale report line.
    existing = {p.parent.name for p in BY_TOPIC_DIR.glob("*/index.qmd")}
    orphans = sorted(existing - set(counts))
    if orphans:
        print(f"NOTE: topic page(s) with no statements any more (not removed automatically): {orphans}")

    if check:
        if stale:
            print(f"{len(stale)} file(s) would be updated:")
            for s in stale:
                print(f"  {s}")
            return 1
        print(f"{len(counts)} topic(s) in use, {len(leaves)} statement(s) checked, all pages current")
        return 0

    print(f"wrote {len(counts)} topic page(s) + overview, updated {len(changed)} file(s) total")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    return run(args.check)


if __name__ == "__main__":
    sys.exit(main())
