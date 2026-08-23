#!/usr/bin/env bash
# verify-loop.sh <campaign-dir> <intermediate-id>
#
# HARNESS 3.5 -> 3.6 -> 3.7 is a fixed-point iteration with three termination
# conditions. Control flow of that shape belongs in a shell, not in a language
# model's working memory: this is where tallies drift, where a revision cycle
# gets miscounted, and where a loop that should have stopped keeps going.
#
# The model makes the judgements (referee, handling editor, reviser). The
# script counts, branches and stops.
#
# Termination (3.5, 3.7):
#   ACCEPT   5 clean passes                       -> freeze
#   REFUTE   two independent passes report the same critical error,
#            upheld by Triage                     -> stop, route to Weakener
#   STALL    the same defect survives 3 revision cycles -> stop, human reads it
#   BLOCKED  a load-bearing (E): a library gap, not a proof defect
#                                                 -> stop, fill the source queue

set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
. "$HERE/lib/common.sh"
need_jq; probe_flags

CAMPAIGN="${1:?usage: verify-loop.sh <campaign-dir> <intermediate-id>}"
ID="${2:?usage: verify-loop.sh <campaign-dir> <intermediate-id>}"
MAX_CYCLES="${MAX_CYCLES:-3}"
OUTDIR="$CAMPAIGN/intermediates"
BASE="$ID"          # revisions are BASE-r1, BASE-r2, ... never nested

assert_not_frozen "$CAMPAIGN/LEDGER.md" "$ID"

for cycle in $(seq 1 "$MAX_CYCLES"); do
  log "=== cycle $cycle/$MAX_CYCLES for $ID ==="

  # ---- 1. package + five blind passes ------------------------------------
  "$HERE/blind-package.reference.sh" "$CAMPAIGN" "$ID"
  "$HERE/blind-verify.sh" "$CAMPAIGN" "$ID" 5

  TALLY="$OUTDIR/${ID}-audit-tally.tsv"
  CLEAN=$(awk -F'\t' 'NR>1 && $3=="CLEAN"' "$TALLY" | wc -l | tr -d ' ')
  if [ "$CLEAN" -ge 5 ]; then
    log "ACCEPT: $CLEAN clean passes. Mark ESTABLISHED + FROZEN, evict the proof."
    exit 0
  fi

  # ---- 2. Triage: referee the referees (3.6) ------------------------------
  # Not blind: Triage needs the artifact and every report. It emits one
  # machine-readable control token so the shell can branch on it.
  TRIAGE="$OUTDIR/${ID}-triage-c${cycle}.md"
  {
    cat <<'HDR'
You are the handling editor. Rule each finding on the mathematics alone; the
referee's confidence is not evidence.

  UPHELD        real defect; the artifact must change.
  OVERRULED     referee mistaken; explain the error precisely.
  PEDANTIC      a gap a competent reader fills without effort; note it, do not
                require a rewrite. STATEMENT DRIFT (A) is never PEDANTIC.
  NEEDS SOURCE  cannot be settled without an unreachable source; route to the
                source queue, NOT to the reviser.
  UNCLEAR       cannot adjudicate; escalate to the human.

OUTPUT: the filtered report (UPHELD + PEDANTIC only); the escalation list; a
consolidated SOURCE REQUEST with duplicates merged. Then, as the last line and
nothing after it:

### LOOP CONTROL ###
DECISION: ACCEPT | REVISE | REFUTE | ESCALATE | BLOCKED_ON_SOURCE

Choose REFUTE when two or more independent referees report the same critical
error and you uphold it: stop revising at once rather than grinding the cycle
budget. Choose BLOCKED_ON_SOURCE when a load-bearing (E) is the binding
constraint: that is a gap in the library, not in the proof.
HDR
    printf '\n### PROBLEM CONTRACT ###\n\n'; cat "$OUTDIR/${ID}-audit-files/CONTRACT.md"
    printf '\n### ARTIFACT ###\n\n';         cat "$OUTDIR/${ID}-audit-files/ARTIFACT.md"
    printf '\n### REFEREE REPORTS ###\n\n'
    for r in "$OUTDIR/${ID}"-audit-response-*.md; do
      printf '\n--- report %s ---\n' "$(basename "$r")"; cat "$r"
    done
  } | "$CLAUDE_BIN" -p --model opus --output-format json \
        ${HAS_EFFORT:+--effort medium} --permission-mode dontAsk \
        --max-turns 4 | jq -r '.result' > "$TRIAGE"

  DECISION="$(grep -m1 -oE 'DECISION:[[:space:]]*[A-Z_]+' "$TRIAGE" | awk '{print $2}' || true)"
  log "triage decision: ${DECISION:-UNPARSED}  ($TRIAGE)"

  case "${DECISION:-UNPARSED}" in
    ACCEPT)  log "Triage overruled every finding. Re-run blind passes to reach the tally."; continue ;;
    REFUTE)  log "STOP: approach refuted. Route to a fresh plan or the Weakener (3.10)."; exit 2 ;;
    ESCALATE|UNPARSED)
             log "STOP: escalated to you. Read $TRIAGE."; exit 3 ;;
    BLOCKED_ON_SOURCE)
             log "STOP: blocked on a source. Fill the queue at the next SOURCE GATE."; exit 4 ;;
    REVISE)  : ;;
  esac

  # ---- 3. Reviser (3.7): new monotone id, never overwrite ----------------
  NEXT="${BASE}-r${cycle}"
  {
    cat <<'HDR'
Repair the artifact.
* Address every UPHELD finding; change nothing unflagged.
* You may NOT close a gap by weakening the theorem. If the only repair weakens
  it, STOP and report that; weakening goes through the Weakener gate (3.10),
  which is the human's to choose. The original claim then reverts to unproved.
* Any [SOURCE-BLOCKED] marker stays; you have no more literature access than
  before. If you can route around it entirely, do so and say so.
* Do not paper over a gap with prose; supply the argument or leave [GAP] marked.
Return the FULL revised artifact, ending with its END-OF-ARTIFACT marker, then
a changelog mapping each finding to its resolution.
HDR
    printf '\n### PROBLEM CONTRACT ###\n\n'; cat "$OUTDIR/${ID}-audit-files/CONTRACT.md"
    printf '\n### ARTIFACT ###\n\n';         cat "$OUTDIR/${ID}-audit-files/ARTIFACT.md"
    printf '\n### FILTERED REPORT ###\n\n';  cat "$TRIAGE"
  } | "$CLAUDE_BIN" -p --model opus --output-format json \
        ${HAS_EFFORT:+--effort high} --permission-mode dontAsk \
        --max-turns 6 | jq -r '.result' > "$OUTDIR/${NEXT}.md"

  log "revised artifact: $OUTDIR/${NEXT}.md"
  ID="$NEXT"          # monotone id; the tally for the new id starts fresh
done

log "STALL: $MAX_CYCLES revision cycles exhausted. A real difficulty lives here."
log "Read the artifact and the triage reports yourself before spending more."
exit 5
