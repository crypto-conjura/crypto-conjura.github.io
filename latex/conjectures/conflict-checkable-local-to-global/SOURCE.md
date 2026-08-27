# Provenance: Conflict Checkable Codes with Local-to-Global Consistency Beyond Half the Singleton Bound

Written in-session following `prompts/harvest.md`; `scripts/harvest_conjectures.py`
could not run its model stage on this machine. Nothing here was checked by a
human yet; this file is what the run believed and why.

## Source

- Paper: **Conflict Checkable and Decodable Codes and Their Applications**
- Authors: Benny Applebaum, Eliran Kachlon
- Venue/archive: IACR ePrint 2023
- Identifier: IACR ePrint 2023/627
- Bibliographic detail: inferred
- File: `2023-627.pdf` (63 pages)
- sha256: `86e57d7a1b69afec45761529c20cb49e9c092bdfd2ee37a58589e5c31b95956e`
- Read on 2026-08-27T21:15:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and this file are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-conjectures`. Theorem 1.8 proves k <= (n-d+2)/2 for codes that are both comparison-based and local-to-global consistent. Theorem 1.3 gives an almost-MDS conflict checkable code at k >= n-d+1-epsilon which bypasses that bound, but it is neither comparison-based nor known to be local-to-global consistent. The conjecture names comparison-basedness as the culprit.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. Where `found` differs from the claimed page, the claim was
wrong and the found page is what the statement cites.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 11 | 11 | exact (100%) | We conjecture that the former property is the important one and that the bound from Theorem 1.8 can be bypassed by some conflict checkable code with local-to-gl |
| endpoint | 11 | 11 | exact (100%) | Observe that this conjecture holds for the special case of d = n − 1 since, in this case, the conflict checkable code from Theorem 1.3 trivially satisfies local |
| candidate | 10 | 10 | exact (100%) | We do not know whether the code from Theorem 1.3 satisfies local-to-global consistency. |
| bound | 11 | 11 | exact (100%) | For every (n, k, d)q comparison-based conflict checkable code with 1 < d < n that satisfies local-to-global consistency, it holds that k ≤ |
| neighbour | 15 | 15 | exact (100%) | The question of finding an exact vertex cover in polynomial-time algorithm in such graphs remains as an interesting open question. |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The conjecture is verbatim on page 11 but phrased in the source as an attribution of blame ('the former property is the important one'), which needs the antecedent resolved to be a standalone statement; the statement spells out that 'the former' is comparison-basedness and states the existential claim explicitly. The source's own note that the conjecture already holds at d = n-1 is recorded prominently rather than buried, since it means the statement is not open across the whole parameter range. One page correction: the vertex-cover neighbour quote is on page 15, not 11.

## Build

`pdflatex` clean; `chktex -q` 0 warnings under the per-folder `.chktexrc`
(every suppression documented in that file, checked hit by hit);
`lacheck` silent.
