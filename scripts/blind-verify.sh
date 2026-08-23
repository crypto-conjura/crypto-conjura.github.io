#!/usr/bin/env bash
# blind-verify.sh <campaign-dir> <intermediate-id> [n-passes]
#
# Replaces the manual step in HARNESS 3.5.1: "open a CLEAN session, drag in
# I0N-audit-files/, paste I0N-audit-prompt.txt, save the verdict".
#
# Each pass is a separate OS process, started with --bare in an empty scratch
# directory, so its context window contains exactly the Contract, the source
# cards, the artifact and the referee prompt. Nothing else: no CLAUDE.md, no
# auto memory, no skills, no plugins, no MCP servers, no prior verdicts, no
# generator trace. The blindness invariant becomes a property of the process,
# not a promise you made to a chat window.
#
# Outputs, per pass p:
#   <id>-audit-response-p.md    the referee report, verbatim
#   <id>-audit-raw-p.json       envelope: model, cost, session id, duration
#   <id>-audit-tally.tsv        pass / model / status / cost, appended
#
# Env:
#   VERIFIER_MODELS   space-separated, cycled over passes  (default below)
#   VERIFIER_EFFORT   default high      (3.5: five high passes beat one max)
#   MAX_BUDGET_USD    optional per-pass cap
#   FORCE=1           override the FROZEN guard

set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
. "$HERE/lib/common.sh"
need_jq; probe_flags; require_api_key

CAMPAIGN="${1:?usage: blind-verify.sh <campaign-dir> <intermediate-id> [n]}"
ID="${2:?usage: blind-verify.sh <campaign-dir> <intermediate-id> [n]}"
N="${3:-5}"

PKG="$CAMPAIGN/intermediates/${ID}-audit-files"
OUTDIR="$CAMPAIGN/intermediates"
TALLY="$OUTDIR/${ID}-audit-tally.tsv"

[ -d "$PKG" ] || die "no audit package at $PKG (run blind-package.sh first)"
for f in CONTRACT.md ARTIFACT.md REFEREE-PROMPT.md; do
  [ -f "$PKG/$f" ] || die "package is missing $f"
done
assert_not_frozen "$CAMPAIGN/LEDGER.md" "$ID"

# Model diversity is the whole point of five passes. Five samples from one
# model are one referee sampled five times: correlated errors survive them all
# (HARNESS 1, invariant "Isolation"; 3.7, the cognitive well). Vary the model,
# and for at least one certifying pass use a different family entirely by
# setting EXTERNAL_VERIFIER_CMD below.
read -r -a MODELS <<<"${VERIFIER_MODELS:-opus sonnet opus sonnet opus}"
EFFORT="${VERIFIER_EFFORT:-high}"

# ---- assemble the single blind prompt, once, byte-identical for every pass --
BLIND_PROMPT="$(mktemp)"
{
  cat "$PKG/REFEREE-PROMPT.md"
  printf '\n\n### PROBLEM CONTRACT ###\n\n'
  cat "$PKG/CONTRACT.md"
  if compgen -G "$PKG/cards/*.md" >/dev/null; then
    printf '\n\n### SOURCE CARDS ###\n\n'
    cat "$PKG"/cards/*.md
  fi
  printf '\n\n### ARTIFACT UNDER REVIEW ###\n\n'
  cat "$PKG/ARTIFACT.md"
} > "$BLIND_PROMPT"

# Guard against the failure this whole exercise exists to prevent: a package
# that leaks provenance back into the "blind" context. HARD patterns name
# campaign machinery that cannot legitimately appear in a Contract or a proof.
# SOFT patterns are words that also occur in ordinary mathematics ("cycle",
# "plan"), so they warn rather than stop.
HARD='LEDGER\.md|DEAD PLANS|WEAKENING POOL|RETREAT LOG|SESSION-?LOG|prior verdict|A0[0-9]+-[a-z]+-c[0-9]+|^(agent|model|cycle|status):'
SOFT='prover|refuter|strategist|weakener|triage|verification tally'
if grep -qE "$HARD" "$BLIND_PROMPT"; then
  log "the blind prompt contains campaign machinery:"
  grep -nE "$HARD" "$BLIND_PROMPT" >&2 || true
  [ "${FORCE:-0}" = 1 ] || die "refusing to run a leaky blind package (FORCE=1 to override)"
fi
if grep -qiE "$SOFT" "$BLIND_PROMPT"; then
  log "WARNING: possible role names in the blind prompt; check these are mathematics:"
  grep -niE "$SOFT" "$BLIND_PROMPT" >&2 || true
fi

log "blind prompt: $(wc -w < "$BLIND_PROMPT") words, $N passes, effort=$EFFORT"
[ -f "$TALLY" ] || printf 'pass\tmodel\tstatus\tcost_usd\tresponse\n' > "$TALLY"

# ---- run the passes -------------------------------------------------------
for p in $(seq 1 "$N"); do
  MODEL="${MODELS[$(( (p-1) % ${#MODELS[@]} ))]}"
  RAW="$OUTDIR/${ID}-audit-raw-${p}.json"
  RSP="$OUTDIR/${ID}-audit-response-${p}.md"

  if [ -f "$RSP" ] && [ "${FORCE:-0}" != 1 ]; then
    log "pass $p already recorded ($RSP); skipping. FORCE=1 to redo."
    continue
  fi

  SCRATCH="$(mktemp -d)"                 # empty cwd: nothing local to discover
  blind_flags "$MODEL" "$EFFORT"
  log "pass $p/$N  model=$MODEL  scratch=$SCRATCH"

  # One process = one atomic unit (2.2). If it exits non-zero, nothing is
  # recorded and the pass does not count toward the tally.
  if ( cd "$SCRATCH" && "$CLAUDE_BIN" "${CLAUDE_FLAGS[@]}" < "$BLIND_PROMPT" ) > "$RAW"; then
    result_text "$RAW" > "$RSP"
    STATUS="$(grep -m1 -oE 'STATUS:[[:space:]]*(CLEAN|DEFECTS|TRUNCATED)' "$RSP" \
              | awk '{print $2}' || true)"
    STATUS="${STATUS:-UNPARSED}"
    COST="$(result_cost "$RAW")"
    printf '%s\t%s\t%s\t%s\t%s\n' "$p" "$MODEL" "$STATUS" "$COST" "$(basename "$RSP")" >> "$TALLY"
    log "pass $p -> $STATUS  (\$$COST)"
  else
    log "pass $p FAILED; not recorded"
    rm -f "$RAW"
  fi
  rm -rf "$SCRATCH"
done
rm -f "$BLIND_PROMPT"

# ---- report ---------------------------------------------------------------
CLEAN=$(awk -F'\t' 'NR>1 && $3=="CLEAN"' "$TALLY" | wc -l | tr -d ' ')
TOTAL=$(awk -F'\t' 'NR>1' "$TALLY" | wc -l | tr -d ' ')
SPEND=$(awk -F'\t' 'NR>1 {s+=$4} END {printf "%.4f", s+0}' "$TALLY")

echo
echo "TALLY for $ID (cumulative, never restarted):"
if command -v column >/dev/null 2>&1; then
  column -t -s $'\t' "$TALLY"
else
  awk -F'\t' '{printf "%-5s %-10s %-10s %-9s %s\n", $1, $2, $3, $4, $5}' "$TALLY"
fi
echo
echo "clean passes: $CLEAN / $TOTAL   spend: \$$SPEND"
[ "$CLEAN" -ge 5 ] \
  && echo "ACCEPTANCE MET (>=5 clean). Next: Triage the reports, then FREEZE." \
  || echo "NOT ACCEPTED. Next: triage.sh, then reviser, then re-verify."

# For the strongest form of 3.5.1, add one pass from a different model family:
#   EXTERNAL_VERIFIER_CMD='codex exec --model gpt-5 -'   (or any vendor CLI)
# reading the same blind prompt on stdin and writing to
#   ${ID}-audit-response-ext.md. Record it in the tally by hand with the
# vendor and model named, since a cross-family pass is worth more than a
# same-family one and the Ledger should say which is which.
