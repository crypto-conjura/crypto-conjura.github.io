#!/usr/bin/env bash
# blind-package.reference.sh <campaign-dir> <intermediate-id>
#
# Reference implementation. If you already have blind-package.sh, keep yours;
# blind-verify.sh only requires that the package directory contain:
#     CONTRACT.md          the Problem Contract, verbatim
#     ARTIFACT.md          the proof, provenance stripped, END-OF-ARTIFACT line
#     cards/S*.md          source cards for every cited external result
#     REFEREE-PROMPT.md    the self-contained referee prompt (3.5 + 3.5.1)
#
# What it MUST omit (2.4, 3.5.1): the ledger, the plans, dead ends, prover
# reasoning, prior verdicts, the session log, and any filename or header that
# reveals which agent, model or cycle produced the artifact.

set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
. "$HERE/lib/common.sh"

CAMPAIGN="${1:?usage: blind-package.sh <campaign-dir> <intermediate-id>}"
ID="${2:?usage: blind-package.sh <campaign-dir> <intermediate-id>}"

SRC="$CAMPAIGN/intermediates"
OUT="$CAMPAIGN/intermediates/${ID}-audit-files"
rm -rf "$OUT"; mkdir -p "$OUT/cards"

# ---- Contract -------------------------------------------------------------
CONTRACT="$(ls "$CAMPAIGN"/CONTRACT*.md "$CAMPAIGN"/contract*.md 2>/dev/null | head -1 || true)"
[ -n "$CONTRACT" ] || die "no CONTRACT*.md found in $CAMPAIGN"
cp "$CONTRACT" "$OUT/CONTRACT.md"

# ---- Artifact, provenance stripped ---------------------------------------
# Exact id first, then "<id>-<slug>", never an auxiliary file or a later
# revision: packaging I03 must not silently pick up I03-r2 or I03-triage-c1.
ART=""
for cand in "$SRC/$ID.tex" "$SRC/$ID.md"; do
  [ -f "$cand" ] && { ART="$cand"; break; }
done
if [ -z "$ART" ]; then
  ART="$(find "$SRC" -maxdepth 1 -type f \( -name "${ID}-*.tex" -o -name "${ID}-*.md" \) \
         ! -name '*-audit-*' ! -name '*-triage-*' ! -name '*-session*' \
         ! -regex ".*/${ID}-r[0-9]+\..*" | sort | head -1)"
fi
[ -n "$ART" ] || die "no artifact for $ID in $SRC"
log "artifact: $ART"

# Drop the id/agent/model/cycle header block and any 'A0xx-role-cN' provenance.
sed -E \
  -e '/^%?[[:space:]]*(id|agent|model|cycle|status)[[:space:]]*:/Id' \
  -e 's/A0[0-9]+-[a-z]+-c[0-9]+/[redacted]/g' \
  "$ART" > "$OUT/ARTIFACT.md"

grep -q 'END OF ARTIFACT' "$OUT/ARTIFACT.md" \
  || die "artifact has no END-OF-ARTIFACT marker; it may be truncated (3.5 step 0)"

# ---- Source cards ---------------------------------------------------------
if compgen -G "$CAMPAIGN/sources/S*-card.md" > /dev/null; then
  cp "$CAMPAIGN"/sources/S*-card.md "$OUT/cards/"
fi

# ---- Referee prompt -------------------------------------------------------
cat > "$OUT/REFEREE-PROMPT.md" <<'PROMPT'
You are a referee for a top journal. The Problem Contract, the artifact under
review, and source cards for every external result it cites are supplied below.
Find and report defects.

You are a VERIFIER, NOT A SOLVER: do not repair, fill gaps, or supply the
intended argument. A correct conclusion reached via an unjustified step is
incorrect.

STEP 0 COMPLETENESS: if the artifact lacks its "### END OF ARTIFACT id ###"
line or stops mid-proof, return the single verdict TRUNCATED, name the last
complete unit, and STOP.

Then classify every defect:
 (A) STATEMENT DRIFT: proves something other than the Contract (strengthened
     hypothesis, weakened conclusion, reordered quantifiers, asymptotic for
     exact, an ambiguous term read the easy or vacuous way). CHECK THIS FIRST:
     state what the artifact actually proves, in your own words, and diff it
     against the Contract. Highest-frequency defect.
 (B) CRITICAL ERROR: a broken step. Explain it, note that it invalidates this
     line, then scan on and verify logically independent parts.
 (C) JUSTIFICATION GAP: the conclusion may hold but the argument is incomplete.
     Explain the gap, ASSUME the conclusion, continue downstream.
 (D) CITATION DEFECT: an external result misused. Check against the source
     card hypothesis by hypothesis; confirm our objects satisfy each.
 (E) UNVERIFIABLE: you cannot reach a cited source and no card covers it. Do
     NOT guess or wave through. Record it and say what the proof needs it to
     say. A load-bearing (E) blocks acceptance.

Probe actively for: quantifier order swapped, or "for all sufficiently large n"
silently dropped; a union or probability bound summed over an n-dependent or
unbounded index without control; worst-case vs expected vs high-probability
conflated; an asymptotic claim standing in for an explicit constant the result
needs; a reduction or hybrid whose lost factor or step count is unaccounted
for; an adversary or oracle given access it should not have; a simulation
claimed rather than shown statistically close; independence assumed between
variables not shown independent; a limit, sum-integral or expectation
interchange used without justification; a negligible or measure-zero exception
treated as empty; induction with a missing base case; an object constructed but
not shown to satisfy every required property.

OUTPUT, in this order and nothing else:

### VERDICT ###
STATUS: CLEAN | DEFECTS | TRUNCATED
One sentence of justification.

### FINDINGS ###
| quoted location | class A-E | explanation |

### STEP LOG ###
One line per accepted step; full detail per defect.

### SOURCE REQUEST ###
For (D)/(E) only, or the single word: none

Emit STATUS: CLEAN only if you found no defect of class A, B, D, or a
load-bearing E. A (C) you judge to be a routine gap a competent reader fills
without effort should be reported but does not by itself force DEFECTS; say so
explicitly if you make that call.
PROMPT

log "package written: $OUT"
log "contents: $(cd "$OUT" && find . -type f | tr '\n' ' ')"
