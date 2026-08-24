# GROUNDING RESULT — quotations in 0048-RKHS-1-r2 vs card S1 and the source PDF

Method: every blockquote in card S1 and every string in the artifact introduced
as "verbatim" was normalised (backticks, emphasis and whitespace collapsed) and
compared, first against the PDF text layer (`pdftotext -layout`), then card
against artifact by longest-matching-block diff. Pure-prose passages ground
EXACT against the PDF; passages carrying inline mathematics ground NEAR only
because `pdftotext` breaks formulae across lines, so PDF-grounding alone cannot
distinguish a mangled formula from a dropped clause. The card-vs-artifact diff
can, and is what the findings below rest on.

## Material omissions in the artifact's "verbatim" quotations — 2

* **Footnote 7 (card item Q6).** The artifact's quotation stops after the
  Gavinsky–Lovett sentence and silently drops the closing clause, which the card
  and the PDF both carry:

  > In this paper we are more concerned with rectangles whose distance to being
  > rank one (or monochromatic) is some `ε > 0` that is only a small constant or
  > `1/ polylog(n)`.

* **§2.3 normalisation (card item Q8).** The artifact's quotation drops the
  parenthetical that immediately follows in the card and the PDF:

  > (This restriction is easy to lift and anyway holds automatically in our
  > intended application.)

## Cosmetic only — no material change

* Q2: a trailing full stop added.
* Q5: typographic double quotes rendered as single quotes.

## Not a defect (artefact of this check, recorded so it is not re-raised)

* Q1 appeared to drop the "A positive solution ... would be very interesting"
  paragraph. It does not: card item Q1 holds two separate blockquotes under one
  heading, which the parser merged, and the artifact quotes both, separately and
  in full.

## Card status

Card S1 requires no repair: it carries every clause above in full, including the
two the artifact dropped. The repair, if triage upholds it, belongs to the
artifact.
