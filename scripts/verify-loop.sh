#!/usr/bin/env bash
# verify-loop.sh <campaign-dir> <intermediate-id>
#
# The orchestrator the /audit skill calls. It owns three things and nothing
# else: the FROZEN guard, the acceptance quorum, and the termination condition
# reported as an exit code. Executing the passes is delegated:
#
#   * DEFAULT (preferred). blind-verify.sh runs each pass as a separate OS
#     process under --bare in an empty scratch dir, so blindness is a property
#     of the process. Requires the claude CLI on PATH and ANTHROPIC_API_KEY.
#
#   * IN_SESSION_RESPONSES=<dir>. Degraded fallback for a host with no model
#     backend. The caller runs the passes as in-session subagents and drops
#     their verbatim reports in <dir> as response-<pass>-<angle>.md; this script
#     only tallies what it finds. It is NOT 3.5.1-blind: in-session subagents
#     share one vendor and run with the repo as cwd, so the tally is stamped
#     with that caveat and such rows must never be pooled with --bare rows when
#     judging acceptance. See the c/0010 round-2 tally for the precedent.
#
# This script NEVER writes a verdict of its own. A pass with no parsable
# STATUS line is recorded as UNPARSED and does not count toward the quorum.
#
# Exit codes (the /audit skill reports these verbatim):
#   0 ACCEPT             >= REQUIRED_CLEAN clean passes, no load-bearing (E)
#   2 REFUTE             a pass refutes the Contract statement itself
#   3 ESCALATE           defects recorded; triage report written; revision due
#   4 BLOCKED_ON_SOURCE  a load-bearing (E) / non-empty SOURCE REQUEST
#   5 STALL              nothing new recorded, or every pass aborted
#
# Env: REQUIRED_CLEAN (default 5), VERIFIER_MODELS, VERIFIER_EFFORT, FORCE=1

set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
. "$HERE/lib/common.sh"

CAMPAIGN="${1:?usage: verify-loop.sh <campaign-dir> <intermediate-id>}"
ID="${2:?usage: verify-loop.sh <campaign-dir> <intermediate-id>}"
REQUIRED_CLEAN="${REQUIRED_CLEAN:-5}"

OUTDIR="$CAMPAIGN/intermediates"
TALLY="$OUTDIR/${ID}-audit-tally.tsv"
TRIAGE="$OUTDIR/${ID}-triage.md"
[ -d "$OUTDIR" ] || die "no intermediates dir at $OUTDIR"

# ---- FROZEN guard. A frozen id is re-opened only as a new corrected id. -----
if [ -f "$CAMPAIGN/LEDGER.md" ]; then
  assert_not_frozen "$CAMPAIGN/LEDGER.md" "$ID"
elif grep -qsE "^[[:space:]]*FROZEN[[:space:]]*:?[[:space:]]*$ID\b" "$OUTDIR/${ID}.md" 2>/dev/null; then
  die "$ID is FROZEN; re-open only as a new corrected id"
fi

# ---- run or ingest the passes ----------------------------------------------
if [ -n "${IN_SESSION_RESPONSES:-}" ]; then
  RSPDIR="$IN_SESSION_RESPONSES"
  [ -d "$RSPDIR" ] || die "IN_SESSION_RESPONSES=$RSPDIR is not a directory"
  compgen -G "$RSPDIR/response-*.md" >/dev/null \
    || die "no response-*.md in $RSPDIR; nothing to tally (this script does not generate verdicts)"

  if [ ! -f "$TALLY" ]; then
    {
      printf '# NOT 3.5.1-blind: in-session subagents, one vendor, repo as cwd.\n'
      printf '# Fresh contexts per pass (no generator trace), package staged outside\n'
      printf '# the repo and neutrally named. Do NOT pool these rows with --bare rows.\n'
      printf '# Cumulative; never restarted.\n'
      printf 'pass\tmodel\tstatus\tcost_usd\tresponse\n'
    } > "$TALLY"
  fi

  for f in "$RSPDIR"/response-*.md; do
    base="$(basename "$f")"
    pass="$(printf '%s' "$base" | sed -E 's/^response-([^-]+)-.*/\1/')"
    if awk -F'\t' -v p="$pass" 'NR>1 && $1==p {found=1} END{exit !found}' "$TALLY" \
       && [ "${FORCE:-0}" != 1 ]; then
      log "pass $pass already recorded; not re-run (tally is cumulative)"
      continue
    fi
    model="$(sed -nE 's/^MODEL:[[:space:]]*(.+)$/\1/p' "$f" | head -1)"
    status="$(grep -m1 -oE 'STATUS:[[:space:]]*(CLEAN|DEFECTS|TRUNCATED)' "$f" | awk '{print $2}' || true)"
    cp "$f" "$OUTDIR/${ID}-audit-${base}"
    printf '%s\t%s\t%s\t%s\t%s\n' \
      "$pass" "${model:-unknown}" "${status:-UNPARSED}" "n/a" "${ID}-audit-${base}" >> "$TALLY"
    log "pass $pass -> ${status:-UNPARSED}  (model ${model:-unknown})"
  done
else
  probe_flags; require_api_key
  "$HERE/blind-verify.sh" "$CAMPAIGN" "$ID" "$REQUIRED_CLEAN"
fi

# ---- quorum ----------------------------------------------------------------
CLEAN=$(awk -F'\t' '$1!~/^#/ && NR>1 && $3=="CLEAN"' "$TALLY" | wc -l | tr -d ' ')
TOTAL=$(awk -F'\t' '$1!~/^#/ && $1!="pass" && NF>=3' "$TALLY" | wc -l | tr -d ' ')
ABORT=$(awk -F'\t' '$1!~/^#/ && ($3=="UNPARSED"||$3=="TRUNCATED")' "$TALLY" | wc -l | tr -d ' ')
SPEND=$(awk -F'\t' '$1!~/^#/ && $4+0==$4 {s+=$4} END {printf "%.4f", s+0}' "$TALLY")

RESPONSES=$(awk -F'\t' '$1!~/^#/ && $1!="pass" && NF>=5 {print $5}' "$TALLY")
REFUTED=0; SRCBLOCK=0
for rel in $RESPONSES; do
  f="$OUTDIR/$rel"; [ -f "$f" ] || continue
  grep -qiE 'CONTRACT REFUTED|the statement is false|counterexample (to|refuting) the (Contract|statement)' "$f" && REFUTED=1
  # A load-bearing (E) is detected STRUCTURALLY: a findings-table row whose
  # class cell is E. Never by prose matching on "load-bearing" -- the referee
  # prompt itself contains that phrase, so referees echo and negate it, and a
  # substring match cannot tell an assertion from a denial. A non-empty SOURCE
  # REQUEST alone is information for triage, not grounds to block.
  if awk -F'|' '/^\|/ { for(i=1;i<=NF;i++){ gsub(/^[ \t]+|[ \t]+$/,"",$i);
        if($i=="E"||$i=="(E)"){exit 1} } }' "$f"; then :; else SRCBLOCK=1; fi
done

echo
echo "TALLY for $ID (cumulative, never restarted):"
if command -v column >/dev/null 2>&1; then column -t -s $'\t' "$TALLY"; else cat "$TALLY"; fi
echo
echo "clean passes: $CLEAN / $TOTAL   aborted/unparsed: $ABORT   metered spend: \$$SPEND"

# ---- termination condition -------------------------------------------------
if [ "$REFUTED" = 1 ]; then
  echo "TERMINATION: REFUTE (2)"; exit 2
fi
if [ "$SRCBLOCK" = 1 ]; then
  echo "TERMINATION: BLOCKED_ON_SOURCE (4)"; exit 4
fi
if [ "$CLEAN" -ge "$REQUIRED_CLEAN" ]; then
  echo "TERMINATION: ACCEPT (0). Next: triage the reports for record, then FREEZE."
  exit 0
fi
if [ "$TOTAL" -eq 0 ] || [ "$ABORT" -eq "$TOTAL" ]; then
  echo "TERMINATION: STALL (5)"; exit 5
fi

{
  printf '# TRIAGE — %s\n\n' "$ID"
  printf 'Quorum not met: %s clean of %s (need %s).\n\n' "$CLEAN" "$TOTAL" "$REQUIRED_CLEAN"
  printf 'Adjudicate every finding below UPHELD / OVERRULED / PEDANTIC / NEEDS SOURCE\n'
  printf 'before any revision. Reports, in tally order:\n\n'
  for rel in $RESPONSES; do printf -- '- %s\n' "$rel"; done
} > "$TRIAGE"
echo "TERMINATION: ESCALATE (3). Triage report: $TRIAGE"
exit 3
