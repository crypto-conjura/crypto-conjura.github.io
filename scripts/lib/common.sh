#!/usr/bin/env bash
# common.sh - shared helpers for the HARNESS automation scripts.
# Source, do not execute:  . "$(dirname "$0")/lib/common.sh"

set -euo pipefail

# ---------------------------------------------------------------- logging ---
log()  { printf '[%s] %s\n' "$(date -u +%H:%M:%S)" "$*" >&2; }
die()  { printf 'ERROR: %s\n' "$*" >&2; exit 1; }

# ------------------------------------------------------- capability probe ---
# Claude Code flags move between versions. Probe once, degrade gracefully,
# and never silently drop a flag that changes the meaning of a run.
CLAUDE_BIN="${CLAUDE_BIN:-claude}"

probe_flags() {
  command -v "$CLAUDE_BIN" >/dev/null 2>&1 || die "$CLAUDE_BIN not on PATH"
  CLAUDE_HELP="$("$CLAUDE_BIN" --help 2>&1 || true)"

  # --bare is load-bearing for blindness: it skips CLAUDE.md, auto memory,
  # skills, plugins, hooks and MCP discovery. Without it a "clean" session
  # is not clean. Refuse to fake it.
  HAS_BARE=0;   grep -q -- '--bare'          <<<"$CLAUDE_HELP" && HAS_BARE=1
  HAS_EFFORT=0; grep -q -- '--effort'        <<<"$CLAUDE_HELP" && HAS_EFFORT=1
  HAS_BUDGET=0; grep -q -- '--max-budget-usd'<<<"$CLAUDE_HELP" && HAS_BUDGET=1
  export HAS_BARE HAS_EFFORT HAS_BUDGET
}

# Build the common flag array for a one-shot, context-free run.
# usage: blind_flags <model> <effort>   ->  populates array CLAUDE_FLAGS
blind_flags() {
  local model="$1" effort="$2"
  CLAUDE_FLAGS=(-p --model "$model" --output-format json
                --permission-mode dontAsk --max-turns "${MAX_TURNS:-6}")
  if [ "${HAS_BARE:-0}" = 1 ]; then
    CLAUDE_FLAGS+=(--bare)
  else
    log "WARNING: --bare unavailable; this run may inherit ~/.claude context."
    log "         Blindness is NOT guaranteed. Upgrade Claude Code."
  fi
  [ "${HAS_EFFORT:-0}" = 1 ] && CLAUDE_FLAGS+=(--effort "$effort")
  [ "${HAS_BUDGET:-0}" = 1 ] && [ -n "${MAX_BUDGET_USD:-}" ] \
      && CLAUDE_FLAGS+=(--max-budget-usd "$MAX_BUDGET_USD")
  export CLAUDE_FLAGS
}

# --bare does not read OAuth credentials or the keychain; it needs an API key.
require_api_key() {
  [ "${HAS_BARE:-0}" = 1 ] || return 0
  [ -n "${ANTHROPIC_API_KEY:-}" ] || die \
    "--bare mode does not use your subscription login. Set ANTHROPIC_API_KEY."
}

# ----------------------------------------------------------- freeze guard ---
# 2.4: a statement is verified exactly once. Re-verifying a FROZEN id is the
# fastest way to burn an allowance, so make it cost an explicit --force.
assert_not_frozen() {
  local ledger="$1" id="$2"
  [ -f "$ledger" ] || return 0
  if grep -qE "\b${id}\b.*FROZEN" "$ledger"; then
    [ "${FORCE:-0}" = 1 ] || die \
      "$id is marked FROZEN in $ledger. Re-verification is forbidden by 2.4.
       If a downstream step revealed a mismatch, open a NEW corrected id.
       To override anyway: FORCE=1 $0 ..."
  fi
}

# ------------------------------------------------------------ json helpers --
need_jq() { command -v jq >/dev/null 2>&1 || die "jq is required"; }

# Extract the text result and the client-side cost estimate from a -p run.
result_text() { jq -r '.result // empty' "$1"; }
result_cost() { jq -r '.total_cost_usd // 0'  "$1"; }
