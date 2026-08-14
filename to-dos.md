# To-dos

## 1. Three-tab conjecture pages

Done: every conjecture page (the template and the 3 real write-ups) is now a `::: {.panel-tabset}` with three tabs:

1. **Statement** — the conjecture statement exactly as the page read before (Abstract/definitions/conjecture/state-of-the-art, demoted to `###` sub-sections inside the tab), plus the *statement's* `.tex` source and compiled PDF links.
2. **Proof** — a placeholder, since none of these conjectures are resolved: "This conjecture is open — no proof exists yet," with a note on the convention to follow once one exists (a second `.tex`/PDF pair, e.g. `latex/proof.tex` / `pdf/proof.pdf`).
3. **Formal Artifact** — the Lean *statement* link (`lean/Statement.lean`), with a note that only the statement is formalized so far, not a proof, plus the convention for adding one later (replace the `sorry`, or add `lean/Proof.lean`).

Remaining, if it comes up later: nothing structural — the Proof tab's real content is blocked on someone actually proving one of these conjectures, not on further site work.

## 2. Tag papers by topic

Conjectures are already tagged this way — done: each conjecture carries a `categories: [...]` frontmatter field naming one or more of the 19 preselected topics, and each topic's `index.qmd` is a Quarto `listing` auto-filtered by category, decoupled from which folder the conjecture physically lives in.

Papers don't have this yet (deliberately deferred — there's only one, a template, so far):

- `papers/example-paper/index.qmd` already has the `categories: []` field scaffolded in; populate it the same way conjectures do once there's real content to tag.
- Decide whether papers get their own per-topic listing pages (mirroring `open-problems/<topic>/index.qmd`), or a single `categories: true` filterable listing on `papers/index.qmd` (mirroring how `blog/index.qmd` already does it) — revisit once there's more than one real paper to justify either.

## 3. UC Encyclopedia 

Add a UC tab on the right, uner which there are the following topics listed as a layer heading. Clicking on each when will open a page containing links to a wepage containing information (functionalities, properties, artifacts) related to that functionlity. 

The 100 UC ideal functionalities, in dependency order
Status: S = idealized setup   C = canonical   E = emerging   O = open (no UC formulation)

Layer 0. Idealized setup and resources
  1. F-CRS          Common reference string                                [S]
  2. F-ACRS         Augmented CRS, "sunspots"                              [S]
  3. F-PKI          Public-key infrastructure                              [S]
  4. G-PKI          Global, non-encapsulated PKI                           [S]
  5. F-REG, F-KRK   Key registration, with knowledge                       [S]
  6. F-CERT         Certification authority                                [S]
  7. F-RO           Local random oracle                                    [S]
  8. G-RO           Global RO: observable, programmable, restricted        [C]
  9. G-clock        Clock                                                  [S]
 10. F-syn          Bounded-delay network                                  [S]
 11. F-clocksync    Dynamic ad hoc clock synchronization                   [C]
 12. F-nettime      Attackable network time service                        [C]
 13. F-RP           Ideal cipher, two-sided permutation                    [S]
 14. G-GG           Generic group, global observable; bilinear types 1-3   [S]
 15. F-wrap         Tamper-proof hardware token                            [S]
 16. F-PUF          Physically uncloneable function                        [S]
 17. F-leak         Leakage, physically observable computation             [S]

Layer 1. Channels, agreement, ledgers
 18. F-auth         Authenticated transmission                             [C]
 19. F-smt          Secure message transmission                            [C]
 20. F-sc           Session secure channel                                 [C]
 21. F-split        Unauthenticated channels, split adversary              [C]
 22. F-dauth        On-line deniable authentication                        [C]
 23. F-diffuse      Diffusion, gossip channel                              [C]
 24. F-rbc          Reliable broadcast                                     [C]
 25. F-BC           Broadcast                                              [C]
 26. F-BA           Byzantine agreement                                    [C]
 27. F-ABA          Asynchronous Byzantine agreement                       [C]
 28. F-ledger       Transaction ledger                                     [C]
 29. G-ledger       Global ledger, irreplaceability                        [C]
 30. F-certmail     Certified mail                                         [E]

Layer 2. Cryptographic library and symmetric primitives
 31. F-crypto       Joint-state cryptographic library                      [C]
 32. F-SE           Symmetric encryption, stream cipher                    [C]
 33. F-AE           Authenticated encryption, on-line AE                   [C]
 34. F-fsAEAD       Forward-secure AEAD                                    [C]
 35. F-MAC          Message authentication code                            [C]
 36. F-KDF          Key derivation                                         [C]
 37. F-OWF          One-way function                                       [O]
 38. F-PRG          Pseudorandom generator                                 [O]
 39. F-PRF, F-PRP   Pseudorandom function, permutation                     [E]
 40. F-CRHF         Collision-resistant hashing                            [O]
 41. F-MHF          Memory-hard function, password hashing                 [O]

Layer 3. Public-key primitives, key exchange, messaging
 42. F-PKE          Public-key encryption, KEM                             [C]
 43. F-rPKE         Replayable CCA relaxation                              [C]
 44. F-NCE          Non-committing encryption                              [C]
 45. F-aPKE         Adaptively secure non-interactive PKE                  [C]
 46. F-SIG          Digital signature                                      [C]
 47. F-adsig        Adaptor signature                                      [C]
 48. F-KE           Key exchange, authenticated KE                         [C]
 49. F-DH           Ideal Diffie-Hellman exponentiation                    [C]
 50. F-pwKE         Password-authenticated KE                              [C]
 51. F-aPAKE        Asymmetric PAKE                                        [C]
 52. F-saPAKE       Strong asymmetric PAKE                                 [C]
 53. F-PHE          Password-hardened encryption, threshold, key rotation  [C]
 54. F-CKE          Continuous KE, asymmetric ratchet                      [C]
 55. F-secmsg       End-to-end secure messaging                            [C]
 56. F-CGKA         Continuous group key agreement                          [E]
 57. F-IBE          Identity-based encryption                              [E]
 58. F-ABE          Attribute-based encryption                             [E]
 59. F-FE           Functional, predicate encryption                       [O]
 60. F-FHE          Threshold FHE decryption                               [C]
 61. F-obf          Obfuscation, split VBB, iO                             [O]

Layer 4. Commitments and proofs
 62. F-COM          Commitment                                             [C]
 63. F-MCOM         Multi-session commitment                               [C]
 64. F-NMCOM        Non-malleable commitment                               [C]
 65. F-eqv          Equivocal, adaptively secure commitment                [C]
 66. F-CP           Commit-and-prove                                       [C]
 67. F-ZK           Zero knowledge                                         [C]
 68. F-NIZK         Non-interactive zero knowledge                         [C]
 69. F-SNARK        Witness-succinct UC NIZK                               [C]
 70. F-acc          Accumulator, vector commitment                         [C]

Layer 5. Oblivious transfer and correlated randomness
 71. F-OT           Oblivious transfer                                     [C]
 72. F-COT, F-ROT   Correlated, random OT                                  [C]
 73. F-OLE          Oblivious linear evaluation                            [E]
 74. F-OPRF         Oblivious PRF                                          [C]
 75. F-GC           Garbled circuit                                        [E]
 76. F-PSI          Private set intersection                               [E]
 77. F-PIR          Private information retrieval                          [O]
 78. F-ORAM         Oblivious RAM                                          [O]

Layer 6. Secret sharing, threshold cryptography, MPC
 79. F-VSS          Verifiable secret sharing                              [C]
 80. F-DKG          Distributed key generation                             [C]
 81. F-thdec        Threshold decryption                                   [C]
 82. F-TSIG         Threshold signature                                    [C]
 83. F-ABB          Arithmetic black box                                   [C]
 84. F-SFE          Two-party secure function evaluation                   [C]
 85. F-MPC          n-party secure computation                             [C]
 86. F-fairSFE      Guaranteed output delivery                             [C]
 87. F-asyncMPC     Asynchronous MPC                                       [C]
 88. F-incoerc      Incoercible, receipt-free computation                  [C]
 89. F-coin         Coin tossing                                           [C]
 90. F-beacon       Randomness beacon                                      [C]

Layer 7. Privacy and anonymity
 91. F-mix          Mix-net, verifiable shuffle                            [C]
 92. F-gsig         Group signature                                        [E]
 93. F-bsig         Blind signature                                        [C]
 94. F-rsig         Ring signature                                         [C]
 95. F-cred         Anonymous credential, DAA                              [C]
 96. F-onion        Onion routing                                          [C]
 97. F-VRF          Verifiable random function                             [C]

Layer 8. Time and application composites
 98. F-TLP          Time-lock puzzle, verifiable delay function            [C]
 99. F-chan         State channel, virtual channel                         [C]
100. F-vote         Self-tallying election                                 [C]
