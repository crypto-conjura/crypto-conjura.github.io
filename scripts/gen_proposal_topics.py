#!/usr/bin/env python3
"""Generates StackExchange-style topic-tag chips for projects/proposals/index.qmd
and the tag-cloud/browse page at projects/proposals/by-topic/index.qmd.

Proposals aren't individual files with their own frontmatter the way a
problem statement (c/*/index.qmd) is -- they're all `#### `-level sections on
one page. So unlike scripts/gen_topics.py, there's no per-page frontmatter to
read `topics:` from; the PROPOSALS list below *is* the source of truth,
hand-maintained in the same document order the headings appear in the page.
Run this after adding, removing, or reordering a proposal direction; `--check`
reports drift without writing anything.

Two things are generated, both from PROPOSALS/TOPIC_DESCRIPTIONS below:

  - the managed `<!-- topics:start -->...<!-- topics:end -->` block right
    after every `#### ` heading in projects/proposals/index.qmd: clickable
    chips for that direction's own topics.
  - projects/proposals/by-topic/index.qmd: a single page carrying both the
    tag cloud (sized by count) and, below it, one group per topic listing
    every direction that carries it -- there's no per-topic subpage the way
    problems/by-topic/<slug>/ has one, since 48 short entries don't need 46
    separate listing pages to stay browsable.

    python3 scripts/gen_proposal_topics.py           # write everything
    python3 scripts/gen_proposal_topics.py --check   # report drift, exit 1

The anchor for each entry is pandoc's auto-generated heading id, verified by
actually running `quarto render projects/proposals/index.qmd --to html` and
reading the `data-anchor-id` attributes back out -- not re-derived here,
since pandoc's slugification has edge cases (a leading "3-" in "3-party
NIKE..." is dropped rather than transliterated) that aren't worth
reimplementing. If a heading's wording changes, re-render and re-check the
anchor before re-running this script.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROPOSALS_PAGE = ROOT / "projects" / "proposals" / "index.qmd"
BY_TOPIC_PAGE = ROOT / "projects" / "proposals" / "by-topic" / "index.qmd"

# One entry per `#### ` heading in projects/proposals/index.qmd, in document
# order. `title` is the heading text for display (plain unicode where the
# source heading uses LaTeX math, e.g. zeta rather than $\zeta$ -- this is a
# summary list, not the page itself). `paper` is the title of the `### `
# paper section the entry falls under.
PROPOSALS = [
    {"anchor": "generalizing-beyond-the-iris-and-beyond-the-lab",
     "title": "Generalizing beyond the iris, and beyond the lab",
     "paper": "Fuzzy Extractors are Practical: Cryptographic Strength Key Derivation from the Iris",
     "topics": ["fuzzy-extractors", "biometric-security"]},
    {"anchor": "zeta-sampling-for-puf-based-fuzzy-extractors",
     "title": "ζ-sampling for PUF-based fuzzy extractors",
     "paper": "Fuzzy Extractors are Practical: Cryptographic Strength Key Derivation from the Iris",
     "topics": ["fuzzy-extractors", "physically-uncloneable-functions"]},
    {"anchor": "competitive-collateral-policies-under-condition-dependent-settlement",
     "title": "Competitive collateral policies under condition-dependent settlement",
     "paper": "Competitive Policies for Online Collateral Maintenance",
     "topics": ["online-algorithms", "collateral-management"]},
    {"anchor": "adaptive-dynamic-wallet-and-collateral-policies",
     "title": "Adaptive, dynamic wallet and collateral policies",
     "paper": "Competitive Policies for Online Collateral Maintenance",
     "topics": ["online-algorithms", "collateral-management"]},
    {"anchor": "multi-stage-crooked-indifferentiability",
     "title": "Multi-stage crooked indifferentiability",
     "paper": "Crooked Indifferentiability of the Feistel Construction",
     "topics": ["indifferentiability", "subversion-resistance"]},
    {"anchor": "broader-applications-and-a-practical-construction",
     "title": "Broader applications and a practical construction",
     "paper": "Crooked Indifferentiability of the Feistel Construction",
     "topics": ["indifferentiability", "subversion-resistance"]},
    {"anchor": "tight-consistency-analysis-for-proof-of-stake-ghost",
     "title": "Tight consistency analysis for proof-of-stake GHOST",
     "paper": "A Tight Analysis of GHOST Consistency",
     "topics": ["blockchain-consensus", "proof-of-stake"]},
    {"anchor": "accountable-peg-out",
     "title": "Accountable peg-out",
     "paper": "Cardinal: Bridging Bitcoin with Ownership Preservation",
     "topics": ["blockchain-bridges", "threshold-signatures"]},
    {"anchor": "strengthening-and-transplanting-the-sum-of-squares-entanglement-detection-technique",
     "title": "Strengthening and transplanting the sum-of-squares entanglement-detection technique",
     "paper": "Quantum Entanglement, Sum of Squares, and the Log Rank Conjecture",
     "topics": ["sum-of-squares", "quantum-information"]},
    {"anchor": "a-general-theory-of-computational-hardness",
     "title": "A general theory of computational hardness",
     "paper": "The Complexity of Public-Key Cryptography",
     "topics": ["sum-of-squares", "average-case-hardness"]},
    {"anchor": "other-matching-heuristics-for-tree-construction",
     "title": "Other matching heuristics for tree construction",
     "paper": "Optimizing Trees for Static Searchable Encryption",
     "topics": ["search-trees", "searchable-encryption"]},
    {"anchor": "leakage-from-tree-rearrangement",
     "title": "Leakage from tree rearrangement",
     "paper": "Optimizing Trees for Static Searchable Encryption",
     "topics": ["searchable-encryption", "leakage"]},
    {"anchor": "classifying-hard-distributions-of-low-degree-polynomials",
     "title": "Classifying hard distributions of low-degree polynomials",
     "paper": "Sum-of-Squares Meets Program Obfuscation, Revisited",
     "topics": ["sum-of-squares", "obfuscation"]},
    {"anchor": "a-general-non-black-box-separation-for-pke-from-owfs",
     "title": "A general non-black-box separation for PKE from OWFs",
     "paper": "Limits on the Power of Garbling Techniques for Public-Key Encryption",
     "topics": ["black-box-separations", "one-way-functions"]},
    {"anchor": "escaping-the-perfect-uniqueness-impossibility-for-vdfs",
     "title": "Escaping the perfect-uniqueness impossibility for VDFs",
     "paper": "Can Verifiable Delay Functions be Based on Random Oracles?",
     "topics": ["verifiable-delay-functions", "random-oracle-model"]},
    {"anchor": "a-meaningful-collapse-binding-property-for-non-interactive-commitments",
     "title": "A meaningful collapse-binding property for non-interactive commitments",
     "paper": "How to Base Security on the Perfect/Statistical Binding Property of Quantum Bit Commitment?",
     "topics": ["commitment-schemes", "quantum-cryptography"]},
    {"anchor": "a-general-theory-of-monolithic-black-box-uselessness",
     "title": "A general theory of monolithic black-box uselessness",
     "paper": "Black-Box Uselessness: Composing Separations in Cryptography",
     "topics": ["black-box-separations"]},
    {"anchor": "simulator-based-proofs-for-compressed-permutation-oracles",
     "title": "Simulator-based proofs for compressed permutation oracles",
     "paper": "Compressed Permutation Oracles (And the Collision-Resistance of Sponge/SHA3)",
     "topics": ["compressed-oracle", "indifferentiability"]},
    {"anchor": "adaptive-corruptions-for-everlasting-uc-commitment-from-malicious-pufs",
     "title": "Adaptive corruptions for everlasting UC commitment from malicious PUFs",
     "paper": "Everlasting UC Commitments from Fully Malicious PUFs",
     "topics": ["universal-composability", "physically-uncloneable-functions"]},
    {"anchor": "reusing-the-quantum-heavy-queries-learner-for-other-qrom-separations",
     "title": "Reusing the quantum heavy-queries learner for other QROM separations",
     "paper": "On the Impossibility of Key Agreements from Quantum Random Oracles",
     "topics": ["quantum-random-oracle-model", "black-box-separations"]},
    {"anchor": "communication-complexity-lower-bounds-for-qrom-key-agreement",
     "title": "Communication-complexity lower bounds for QROM key agreement",
     "paper": "On the Impossibility of Key Agreements from Quantum Random Oracles",
     "topics": ["quantum-random-oracle-model", "key-agreement"]},
    {"anchor": "relating-the-polynomial-compatibility-and-aaronsonambainis-conjectures",
     "title": "Relating the Polynomial Compatibility and Aaronson–Ambainis conjectures",
     "paper": "On the Impossibility of Key Agreements from Quantum Random Oracles",
     "topics": ["quantum-query-complexity", "quantum-random-oracle-model"]},
    {"anchor": "leakage-freeness-for-possibly-divergent-programs",
     "title": "Leakage-freeness for possibly-divergent programs",
     "paper": "Leakage-Free Probabilistic Jasmin Programs",
     "topics": ["formal-verification", "leakage"]},
    {"anchor": "the-theoretical-limits-of-publicly-detectable-watermarking",
     "title": "The theoretical limits of publicly-detectable watermarking",
     "paper": "Publicly-Detectable Watermarking for Language Models",
     "topics": ["watermarking"]},
    {"anchor": "new-robustness-notions-for-publicly-detectable-watermarks",
     "title": "New robustness notions for publicly-detectable watermarks",
     "paper": "Publicly-Detectable Watermarking for Language Models",
     "topics": ["watermarking"]},
    {"anchor": "party-nike-from-non-pairing-algebraic-assumptions",
     "title": "3-party NIKE from non-pairing algebraic assumptions",
     "paper": "Fine-Grained Non-Interactive Key-Exchange: Constructions and Lower Bounds",
     "topics": ["non-interactive-key-exchange", "fine-grained-cryptography"]},
    {"anchor": "applying-leakage-freeness-definitions-to-kyber",
     "title": "Applying leakage-freeness definitions to Kyber",
     "paper": "Schnorr Protocol in Jasmin",
     "topics": ["formal-verification", "leakage"]},
    {"anchor": "post-quantum-security-of-permutation-based-hashing",
     "title": "Post-quantum security of permutation-based hashing",
     "paper": "Towards Compressed Permutation Oracles",
     "topics": ["collision-resistant-hashing", "quantum-cryptography"]},
    {"anchor": "a-workable-decompression-operator-for-permutations",
     "title": "A workable decompression operator for permutations",
     "paper": "Towards Compressed Permutation Oracles",
     "topics": ["compressed-oracle"]},
    {"anchor": "extending-the-top-down-ansatz-to-correlated-output-oracles",
     "title": "Extending the top-down ansatz to correlated-output oracles",
     "paper": "Towards Compressed Permutation Oracles",
     "topics": ["compressed-oracle"]},
    {"anchor": "extending-qrom-time-lock-puzzle-impossibility-to-vdfs",
     "title": "Extending QROM time-lock-puzzle impossibility to VDFs",
     "paper": "On the (Im)possibility of Time-Lock Puzzles in the Quantum Random Oracle Model",
     "topics": ["time-lock-puzzles", "verifiable-delay-functions"]},
    {"anchor": "post-quantum-minimality-for-other-primitives",
     "title": "Post-quantum minimality for other primitives",
     "paper": "A Note on the Minimality of One-Way Functions in Post-Quantum Cryptography",
     "topics": ["one-way-functions", "quantum-cryptography"]},
    {"anchor": "porting-dag-based-bft-protocols-to-the-permissionless-adaptive-setting",
     "title": "Porting DAG-based BFT protocols to the permissionless, adaptive setting",
     "paper": "High-Throughput Permissionless Blockchain Consensus under Realistic Network Assumptions",
     "topics": ["byzantine-agreement", "blockchain-consensus"]},
    {"anchor": "a-compact-on-chain-postable-certificate-of-ml-training-work",
     "title": "A compact, on-chain-postable certificate of ML training work",
     "paper": "Efficient and Proof-of-Useful-Work Friendly Local-Search for Distributed Consensus",
     "topics": ["proof-of-work", "blockchain-consensus"]},
    {"anchor": "bypassing-the-round-optimality-barrier-with-a-non-group-assumption",
     "title": "Bypassing the round-optimality barrier with a non-group assumption",
     "paper": "On the Impossibility of Round-Optimal Pairing-Free Blind Signatures in the ROM",
     "topics": ["blind-signatures", "generic-group-model"]},
    {"anchor": "direct-specialized-constructions-for-threshold-signatures-and-encryption",
     "title": "Direct, specialized constructions for threshold signatures and encryption",
     "paper": "Proactive Secret Sharing without Erasures",
     "topics": ["secret-sharing", "threshold-signatures"]},
    {"anchor": "a-seeded-proof-of-work-compatible-with-distributed-samplers",
     "title": "A seeded proof-of-work compatible with distributed samplers",
     "paper": "Permissionless Consensus from a Common Random String",
     "topics": ["proof-of-work", "blockchain-consensus"]},
    {"anchor": "sequential-composition-and-dynamic-difficulty-adjustment",
     "title": "Sequential composition and dynamic difficulty adjustment",
     "paper": "Permissionless Consensus from a Common Random String",
     "topics": ["blockchain-consensus", "proof-of-work"]},
    {"anchor": "removing-the-crs-and-minimizing-assumptions",
     "title": "Removing the CRS and minimizing assumptions",
     "paper": "Permissionless Consensus from a Common Random String",
     "topics": ["blockchain-consensus"]},
    {"anchor": "collusion-that-harms-rather-than-profits",
     "title": "Collusion that harms rather than profits",
     "paper": "Incentivizing Geographic Diversity for Decentralized Systems",
     "topics": ["game-theory", "incentive-mechanisms"]},
    {"anchor": "a-multi-tiered-richer-strategy-space",
     "title": "A multi-tiered, richer strategy space",
     "paper": "Incentivizing Geographic Diversity for Decentralized Systems",
     "topics": ["game-theory", "incentive-mechanisms"]},
    {"anchor": "identifiable-abort-for-tweed",
     "title": "Identifiable abort for Tweed",
     "paper": "Tweed: Adaptively Secure Lattice-Based Two-Round Threshold Signatures",
     "topics": ["threshold-signatures", "learning-with-errors"]},
    {"anchor": "a-meaningful-spv-style-bridge-in-the-papers-formal-model",
     "title": "A meaningful SPV-style bridge in the paper's formal model",
     "paper": "Crossing with Confidence: Formal Analysis and Model Checking of Blockchain Bridges",
     "topics": ["blockchain-bridges", "formal-verification"]},
    {"anchor": "further-security-notions-in-the-same-formal-framework",
     "title": "Further security notions in the same formal framework",
     "paper": "Crossing with Confidence: Formal Analysis and Model Checking of Blockchain Bridges",
     "topics": ["blockchain-bridges", "formal-verification"]},
    {"anchor": "a-tight-qrom-proof-from-a-search-assumption",
     "title": "A tight QROM proof from a search assumption",
     "paper": "Tight Lattice-Based Signatures without Trapdoors from Search LWE",
     "topics": ["signature-schemes", "tight-reductions", "quantum-random-oracle-model"]},
    {"anchor": "extending-tightness-to-the-multi-user-setting",
     "title": "Extending tightness to the multi-user setting",
     "paper": "Tight Lattice-Based Signatures without Trapdoors from Search LWE",
     "topics": ["signature-schemes", "tight-reductions"]},
    {"anchor": "uc-realizations-with-many-bulletin-board-managers",
     "title": "UC realizations with many bulletin-board managers",
     "paper": "Beyond Blockchain Ballots: UC-Secure Layer-2 Voting and Governance",
     "topics": ["universal-composability", "voting-and-governance"]},
    {"anchor": "modeling-monetary-stakes-and-a-game-theoretic-incentive-analysis",
     "title": "Modeling monetary stakes and a game-theoretic incentive analysis",
     "paper": "Beyond Blockchain Ballots: UC-Secure Layer-2 Voting and Governance",
     "topics": ["voting-and-governance", "game-theory"]},
]

# One sentence each: the tag-wiki text shown above a topic's group on the
# by-topic page. Every slug used in PROPOSALS must have one, and every one
# here must be used -- checked at the bottom of run(), the same invariant
# scripts/gen_topics.py keeps for TOPIC_DESCRIPTIONS/TOPIC_SLUGS.
TOPIC_DESCRIPTIONS = {
    "fuzzy-extractors": "Extracting a stable cryptographic key from a noisy secret such as a biometric reading or a PUF response.",
    "biometric-security": "Security and reliability of key derivation from a specific biometric modality, and how it holds up outside curated lab conditions.",
    "physically-uncloneable-functions": "Protocols built from hardware tokens whose physical structure cannot be efficiently cloned.",
    "online-algorithms": "Algorithms that commit to each decision as it arrives, analyzed by their competitive ratio against an optimal offline policy.",
    "collateral-management": "Policies for sizing and maintaining the collateral or liquidity backing a stream of transactions.",
    "indifferentiability": "The indifferentiability framework for showing an idealized construction is as good as the random object it is meant to instantiate.",
    "subversion-resistance": "Security that survives a maliciously implemented or backdoored component, such as a subverted random function.",
    "blockchain-consensus": "Protocols for agreeing on a shared chain or ledger state among mutually distrusting, possibly permissionless, participants.",
    "proof-of-stake": "Consensus protocols where influence over block production is weighted by stake rather than computational work.",
    "blockchain-bridges": "Protocols and their formal security models for moving assets or state between separate blockchains.",
    "threshold-signatures": "Signature schemes distributed across multiple signers under a corruption threshold.",
    "sum-of-squares": "The sum-of-squares semidefinite-programming hierarchy, and its use for rounding algorithms and hardness arguments.",
    "quantum-information": "Entanglement, separability, and other problems studied within quantum information theory.",
    "average-case-hardness": "Hardness of a computational problem on a natural random input distribution, as opposed to worst-case hardness.",
    "search-trees": "Optimal construction of search trees over structured query distributions.",
    "searchable-encryption": "Encrypted search schemes and the tradeoffs among their efficiency, leakage, and index structure.",
    "leakage": "What an implementation or protocol execution reveals beyond its specified output, and how to define or eliminate it.",
    "obfuscation": "Techniques and hardness assumptions for program obfuscation, including candidates built from low-degree polynomials.",
    "black-box-separations": "Impossibility or separation results ruling out a fully black-box construction or reduction between two primitives.",
    "one-way-functions": "The minimal cryptographic assumption, and what it does or does not imply in a black-box sense.",
    "verifiable-delay-functions": "Functions that take a prescribed amount of sequential time to evaluate but are quickly verifiable, and their (un)computational uniqueness.",
    "random-oracle-model": "Statements set in the classical (non-quantum) random oracle model.",
    "commitment-schemes": "Commitment protocols and their binding and hiding properties, including in composable or setup-free settings.",
    "quantum-cryptography": "General security notions, constructions, and separations involving quantum adversaries or quantum information.",
    "compressed-oracle": "Zhandry's compressed-oracle method for tracking a quantum algorithm's queries to a random function or permutation.",
    "universal-composability": "Security definitions and realizations in the UC framework, including under adaptive or malicious setup corruption.",
    "quantum-random-oracle-model": "Statements set in the quantum random oracle model, where the oracle may be queried in superposition.",
    "key-agreement": "Two-party protocols for agreeing on a shared secret, and their black-box (im)possibility from weaker primitives.",
    "quantum-query-complexity": "Upper and lower bounds on the number of quantum queries needed against an oracle-based primitive.",
    "formal-verification": "Machine-checked security proofs and definitions, typically in EasyCrypt or a similar proof assistant, for concrete implementations.",
    "watermarking": "Embedding a detectable, ideally robust and hard-to-remove, mark into a model's or program's output.",
    "non-interactive-key-exchange": "Multi-party key exchange with no interaction, typically analyzed in a generic group model.",
    "fine-grained-cryptography": "Cryptographic constructions based on worst-case, fine-grained hardness assumptions rather than average-case ones.",
    "collision-resistant-hashing": "Collision-resistant hash functions as a primitive, and their relations to other assumptions.",
    "time-lock-puzzles": "Puzzles that hide a value for a controlled, only sequentially reducible, amount of time.",
    "byzantine-agreement": "Consensus protocols tolerating malicious parties, and their resilience bounds.",
    "proof-of-work": "Consensus and incentive mechanisms built on costly, verifiable computational work.",
    "blind-signatures": "Signature schemes that let a signer sign a message without seeing it, and round-complexity lower bounds for them.",
    "generic-group-model": "Statements set in a generic group model (Shoup's or Maurer's), where the adversary accesses group operations only through an oracle.",
    "secret-sharing": "Schemes splitting a secret among parties so that only qualified subsets can reconstruct it, including under proactive refresh.",
    "game-theory": "Strategic behavior of rational or adversarial participants, analyzed via equilibrium or best-response reasoning.",
    "incentive-mechanisms": "Reward and penalty designs meant to make honest behavior the rational choice for participants.",
    "learning-with-errors": "Ring- or Module-LWE-specific hardness questions and the constructions built on them.",
    "signature-schemes": "Digital signature constructions and the tightness of their security reductions.",
    "tight-reductions": "Security reductions whose loss is a constant rather than growing with the adversary's resources.",
    "voting-and-governance": "Protocols for casting, tallying, or governing collective decisions with strong composable security guarantees.",
}


def humanize(slug):
    """Same simple, no-small-words-exception transform as gen_topics.py's
    humanize(), so a chip reads the same whether it names a problem topic or
    a proposal topic."""
    return " ".join(w[:1].upper() + w[1:] for w in slug.split("-") if w)


HEADING_RE = re.compile(
    r'^#### (?P<title>[^\n]+)\n'
    r'(?:<!-- topics:start -->\n<div class="cj-tags cj-page-topics">.*?</div>\n<!-- topics:end -->\n)?',
    re.MULTILINE,
)


def chip_block(topics):
    chips = "".join(
        f'<a class="cj-tag cj-tag-topic" href="/projects/proposals/by-topic/index.qmd#{tp}">{humanize(tp)}</a>'
        for tp in sorted(topics)
    )
    return f'<!-- topics:start -->\n<div class="cj-tags cj-page-topics">{chips}</div>\n<!-- topics:end -->\n'


def update_proposals_page(text):
    counter = {"i": 0}

    def repl(m):
        i = counter["i"]
        if i >= len(PROPOSALS):
            raise ValueError(
                f"projects/proposals/index.qmd has more '#### ' headings than "
                f"PROPOSALS has entries ({len(PROPOSALS)}) -- add the new "
                f"direction(s) to scripts/gen_proposal_topics.py"
            )
        counter["i"] += 1
        return f'#### {m.group("title")}\n{chip_block(PROPOSALS[i]["topics"])}'

    new_text = HEADING_RE.sub(repl, text)
    if counter["i"] != len(PROPOSALS):
        raise ValueError(
            f"PROPOSALS has {len(PROPOSALS)} entries but only "
            f"{counter['i']} '#### ' heading(s) were found in "
            f"projects/proposals/index.qmd -- they've drifted out of sync"
        )
    return new_text


def by_topic_page():
    counts = {}
    groups = {}
    for p in PROPOSALS:
        for tp in p["topics"]:
            counts[tp] = counts.get(tp, 0) + 1
            groups.setdefault(tp, []).append(p)

    unknown = set(counts) - set(TOPIC_DESCRIPTIONS)
    if unknown:
        raise ValueError(f"topics used in PROPOSALS but missing a description: {sorted(unknown)}")
    stale = set(TOPIC_DESCRIPTIONS) - set(counts)
    if stale:
        raise ValueError(f"TOPIC_DESCRIPTIONS has entries no PROPOSALS entry uses: {sorted(stale)}")

    ordered = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    lo, hi = min(counts.values()), max(counts.values())
    span = hi - lo or 1

    cloud_lines = []
    for slug, n in ordered:
        size = 0.85 + 0.85 * (n - lo) / span
        cloud_lines.append(
            f'<a class="cj-tag-cloud-item" href="#{slug}" style="font-size: {size:.2f}em;">'
            f'{humanize(slug)} <span class="cj-tag-count">{n}</span></a>'
        )
    cloud = "\n".join(cloud_lines)

    sections = []
    for slug, n in ordered:
        items = "\n".join(
            f'- [{p["title"]}](/projects/proposals/index.qmd#{p["anchor"]}) -- from *{p["paper"]}*'
            for p in groups[slug]
        )
        sections.append(f"## {humanize(slug)}\n\n{TOPIC_DESCRIPTIONS[slug]}\n\n{items}\n")
    body = "\n".join(sections)

    return f"""---
title: "Proposals by Topic"
---

Every open proposal carries one or more topic tags, StackExchange-style, alongside the paper it comes from. Click a tag below to jump to its group; each entry links back to its full write-up on the [main proposals page](/projects/proposals/index.qmd).

::: {{.cj-tag-cloud}}
{cloud}
:::

{body}"""


def run(check):
    old_text = PROPOSALS_PAGE.read_text(encoding="utf-8")
    new_text = update_proposals_page(old_text)
    new_by_topic = by_topic_page()
    old_by_topic = BY_TOPIC_PAGE.read_text(encoding="utf-8") if BY_TOPIC_PAGE.exists() else None

    stale = []
    if new_text != old_text:
        stale.append(str(PROPOSALS_PAGE.relative_to(ROOT)))
    if new_by_topic != old_by_topic:
        stale.append(str(BY_TOPIC_PAGE.relative_to(ROOT)))

    if check:
        if stale:
            print(f"{len(stale)} file(s) would be updated:")
            for s in stale:
                print(f"  {s}")
            return 1
        print(f"{len(PROPOSALS)} proposal(s) checked, {len(TOPIC_DESCRIPTIONS)} topic(s), all pages current")
        return 0

    if new_text != old_text:
        PROPOSALS_PAGE.write_text(new_text, encoding="utf-8")
    if new_by_topic != old_by_topic:
        BY_TOPIC_PAGE.parent.mkdir(parents=True, exist_ok=True)
        BY_TOPIC_PAGE.write_text(new_by_topic, encoding="utf-8")

    print(f"wrote chips for {len(PROPOSALS)} proposal(s) + by-topic page, updated {len(stale)} file(s)")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    return run(args.check)


if __name__ == "__main__":
    sys.exit(main())
