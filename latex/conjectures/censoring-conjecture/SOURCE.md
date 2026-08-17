# Provenance: The Censoring Conjecture for AES

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **How Fast Does the Inverse Walk Approximate a Random Permutation?**
- Authors: Vishesh Jain, Tianren Liu, Clayton Mizgerd, Angelos Pelecanos, Stefano Tessaro, Vinod Vaikuntanathan
- Venue/archive: Cryptology ePrint Archive 2025
- Identifier: 2024/1795
- Bibliographic detail: inferred
- File: `2024-1795.pdf` (31 pages)
- sha256: `f48ca5e2056ad1951668ee1fe4c62b3c633557082d0fa8d0a69560334e26a992`
- Read on 2026-08-17T02:01:18Z via the `cli` backend

## How the paper leaves it open

`paper-conjectures`. Open. Nothing in the paper proves any instance of the implication; what the paper settles is the hypothesis side, namely the round count needed for the censored construction. The only known censoring theorem in the Markov chain literature, due to Peres and Winkler, applies to a family of chains that excludes block ciphers.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 6 | 6 | exact (100%) | This leads us to conjecture that r-round AES is not less secure than r-round censored AES. |
| statement | 6 | 6 | exact (100%) | If one believes that the mixing layers are useful for AES to achieve pseudorandomness, then it is natural to expect that removing a large fraction of them shoul... |
| openness | 5 | 5 | exact (100%) | It is natural to conjecture that the actual AES cipher is not less secure than its censored counterpart, i.e., additional mixing layers only help, and so one ca... |
| openness | 6 | 6 | exact (100%) | Nevertheless, this censoring result has found many applications, and fully understanding how censoring affects the mixing time of a Markov chain remains an open... |
| parameter | 6 | 6 | exact (100%) | We introduce a small round threshold rthresh to allow the block cipher to enter a “generic” state, and avoid any non-typical behavior that may be happening duri... |
| progress | 6 | 6 | exact (100%) | Their setting is limited to a very specific family of Markov chains (Glauber dynamics in a monotone spin system, when the starting position is an extremal confi... |
| definition | 3 | 3 | exact (100%) | which they cast in terms of a construction they call “censored AES”, which is essentially AES with some of the mixing layers removed. |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

Conjecture 1.4 is genuinely posed on p. 6 and stays open — "censor" appears nowhere in the paper after p. 6, and Sections 2-4 plus all three appendices concern only the INV KAC mixing time. The decisive defect is strength: the paper conjectures the implication for one construction, r-round censored AES with LPTV23's fixed censoring pattern (Figure 3, p. 4), whereas the draft quantifies universally over every censoring set C, and compounds this by hardcoding the final round's linear layer to the identity so that even its "uncensored" cipher contradicts Figure 1. Both are precisely repairable against the paper's text, so the conjecture survives with corrections rather than failing outright.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 6 | Conjecture 1.4 ("Censoring conjecture") is stated verbatim on p. 6, introduced by the paragraph "The Censoring Conjecture". All seven draft quotes are accurate at the pages claimed (pp. 3, 5, 6). |
| openness | pass | 6 | The string "censor" occurs in the full text layer only on pp. 3-6, all within the introduction. Sections 2-4 (Preliminaries, Upper Bound, Lower bound) and Appendices A-C concern only the INV KAC mixing time; nothing revisits, weakens, or resolves the implication. The paper explicitly leaves the general censoring question open on p. 6: "fully understanding how censoring affects the mixing time of a Markov chain remains an open problem." |
| strength | fail | 4 | The paper conjectures the implication for "r-round censored AES" -- one specific construction, namely LPTV23's, in which the mixing layers falling inside each run of consecutive (ARK, INV) that emulates an SPN* S-box are censored (Figure 3 and caption, p. 4; described on p. 3 as "essentially AES with some of the mixing layers removed"). The draft universally quantifies over every censoring set C subset of {1,...,r-1}. This is a strengthening: it asserts the implication for arbitrary censoring patterns, including ones the paper never considers. |
| quantifiers | pass | 6 | The order "for any t, there exists a fixed constant r_thresh > 0, such that for any number of rounds r > r_thresh" is reproduced faithfully, as is r_thresh depending only on t and the direction of the implication (censored hypothesis, uncensored conclusion). The paper leaves epsilon unbound; binding it universally over (0,1) is a fair reading. The spurious quantification over C is recorded under the strength check, not here. |
| attribution | pass | 6 | "This leads us to conjecture that r-round AES is not less secure than r-round censored AES" -- the conjecture is the harvested paper's own, numbered as its Conjecture 1.4, not one it attributes to LPTV23 or anyone else. The draft presents it correctly as the paper's. |
| definitions | fail | 4 | The paper gives no formal definition of censored AES, so the draft's Definition 1 is its own construction. It does not match Figure 1 (p. 4): the draft sets L^C_i = id whenever i is in C OR i = r, so its "uncensored" F^(r)_empty omits the linear layer of the final round. Figure 1 and its caption apply Linear Mixing in every one of the r rounds, followed by a final ARK (r+1 ARK operations total). The draft's F^(r)_empty is therefore not the paper's r-round AES -- by the draft's own terminology it is itself censored, which makes the conclusion of the implication weaker than the paper's. Definition 2 (epsilon-approximate t-wise independence) does agree with Definition 2.1 on p. 9. |
| fabrication | fail | 4 | Three unsupported items. (i) The setting calls SPN* "the construction of Baigneres and Vaudenay [BV05]"; p. 3 attributes the construction AES* to BV05, and the Figure 2 caption (p. 4) says SPN* is [LPTV23]'s term for SPNs with random secret S-boxes. (ii) The setting states Theorem 1.1 without its hypothesis t < 2^{(0.499 - 1/(4k))b}, which the paper does impose (p. 3). (iii) The notation identifies L as "ShiftRows followed by MixColumns"; the paper says only "Linear Mixing" / "maximal-branch-number linear mixing" and never names the AES sublayers. Everything else checks out: Theorem 1.2 (192 rounds, 2^-128, pairwise, p. 3), Corollary 1.3 (p. 6), the Theta(n log n + n log(1/eps)) upper bound and both Omega lower bounds against 4-wise independence (p. 5), and the Peres-Winkler hypotheses (p. 6). All five bibliography entries match the reference list on pp. 23-26, including PW11 having no venue. |
| self-containment | pass | - | The formal statement plus the two supplied definitions would let a reader who has never seen the paper know what object to prove something about and what the target property is. No evidence needed from the paper; the defect is that the self-contained statement is a different statement, which is recorded under strength and definitions. |

### Unsupported by the paper

- The setting attributes SPN* to Baigneres and Vaudenay [BV05]. The paper attributes AES* to [BV05] (p. 3) and identifies SPN* as [LPTV23]'s term for the random-S-box SPN (Figure 2 caption, p. 4).
- The setting states Theorem 1.1's conclusion without its hypothesis t < 2^{(0.499 - 1/(4k))b}, which the paper does impose (p. 3).
- The notation asserts that L is "ShiftRows followed by MixColumns". The paper never names these sublayers anywhere; it refers only to "Linear Mixing" and "maximal-branch-number linear mixing" (pp. 3-6).
- Definition 1's claim that "The case C = empty is (round-key-independent) r-round AES" is false for the definition as written, since that definition still deletes the final round's linear layer, which Figure 1 (p. 4) retains.
- The setting's characterisation of [PW11] as "showing that extra updates cannot speed up mixing" states content the paper does not give; the paper describes only PW11's hypotheses (Glauber dynamics, monotone spin system, extremal starting configuration) and calls it "a censoring result of a similar flavor" (p. 6). This is inferable from the cited title but is not asserted by the paper.

### Corrections the checker asked for

- **formal_statement_latex** — The draft quantifies universally over every censoring set C subset of {1,...,r-1}. The paper's Conjecture 1.4 concerns a single construction, "r-round censored AES", whose censoring pattern is the one fixed by LPTV23 (Figure 3, p. 4): the mixing layers lying inside each run of consecutive (ARK, INV) operations that stands in for one SPN* S-box layer. Quantifying over all C is a strengthening the paper does not pose.
  - suggested: Replace "every censoring set $C \subseteq \{1,\dots,r-1\}$" with the single distinguished set: "...such that for every integer $r > r_{\mathrm{thresh}}$ and every $\varepsilon \in (0,1)$, if $\mathcal{F}^{(r)}_{C^{*}(r)}$ is $\varepsilon$-approximately $t$-wise independent then so is $\mathcal{F}^{(r)}_{\emptyset}$," where $C^{*}(r)$ is the censoring set of $r$-round censored AES, i.e. the rounds whose linear mixing layer falls strictly inside one of the consecutive (ARK, INV) runs used to instantiate a single SPN* S-box layer.
- **definitions_latex** — Definition 1 sets $L^{C}_{i} = \mathrm{id}$ when $i \in C$ \emph{or} $i = r$, so the draft's uncensored cipher $\mathcal{F}^{(r)}_{\emptyset}$ has no linear mixing layer in its final round. The paper's SPN (Figure 1, p. 4, and caption) applies Linear Mixing in every one of the $r$ rounds and then one final ARK, for $r+1$ ARK operations. The draft's $\mathcal{F}^{(r)}_{\emptyset}$ is thus not the paper's $r$-round AES.
  - suggested: $L^{C}_{i} := \mathrm{id}_{\mathbb{F}^{16}}$ if $i \in C$, and $L^{C}_{i} := L$ otherwise, with the censoring set allowed to range over $C \subseteq \{1,\dots,r\}$. Then $\mathcal{F}^{(r)}_{\emptyset}$ applies $L$ in every round, matching Figure 1.
- **setting_latex** — SPN* is attributed to Baigneres and Vaudenay. The paper (p. 3) attributes the construction \emph{AES*} to [BV05]; SPN* is [LPTV23]'s name for the generalisation (Figure 2 caption, p. 4). The same sentence also drops the hypothesis on $t$ carried by Theorem 1.1.
  - suggested: "...sidestep it by analysing SPN*, [LPTV23]'s generalisation of the AES* construction of Baign\`eres and Vaudenay \cite{BV05}, and proving that for $t < 2^{(0.499 - 1/(4k))b}$ a $\Theta(k)$-round SPN* with maximal-branch-number mixing is $2^{-\Theta(bk)}$-approximately $t$-wise independent for $k$ blocks of $b$ bits."
- **notation_latex** — $L$ is described as "ShiftRows followed by MixColumns". The paper never names the AES sublayers; it speaks only of the Linear Mixing step and of maximal-branch-number linear mixing.
  - suggested: "$L : \mathbb{F}^{16} \to \mathbb{F}^{16}$, the linear mixing layer, an $\mathbb{F}_2$-linear bijection with maximal branch number (the paper does not decompose it further)."

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 2 warnings

## What to check hardest

Three places to check hardest. (1) The paper writes "r-round censored AES" for the one specific censoring pattern of Liu-Pelecanos-Tessaro-Vaikuntanathan, in which the mixing layer is retained only once every m rounds; I have made the censoring set C an explicit universally quantified parameter, because that is the only self-contained reading and it matches the paper's own justification that "removing a large fraction of them should only hurt". This is a strengthening: a counterexample at some exotic C would not by itself refute Conjecture 1.4 verbatim, so a solver should treat the LPTV23 pattern as the headline target. (2) The paper's statement does not quantify epsilon explicitly; I read it as universally quantified, and I have made r_thresh depend on t alone, as the paper's phrasing "for any t, there exists a fixed constant" indicates. If the intended reading lets r_thresh depend on epsilon too, the conjecture is weaker than stated here. (3) Round keys are independent and uniform throughout this line of work; the paper flags in a footnote that this is a caveat of the results it builds on. The real AES key schedule is out of scope, and the conjecture says nothing about it. Minor: the paper does not pin down in this document exactly which linear map it calls the AES mixing layer, nor whether the final round carries one; I used ShiftRows followed by MixColumns and dropped the last mixing layer, which is immaterial since composing with a fixed bijection preserves approximate t-wise independence. I am not aware of this conjecture having been resolved, but I have not verified that against work appearing after the paper's September 2025 revision.

