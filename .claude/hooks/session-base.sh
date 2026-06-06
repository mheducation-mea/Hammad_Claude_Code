#!/usr/bin/env bash
# SessionStart hook: record the commit HEAD was at when this session began,
# so the Stop hook can scope "what changed this session". Writes to .git/
# (not committed). Always exits 0 and never blocks.
set -uo pipefail
input=$(cat || true)
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)" || exit 0
cd "$ROOT" || exit 0
sid=$(printf '%s' "$input" | jq -r '.session_id // "default"' 2>/dev/null || echo default)
dir=".git/claude-memory-hook"
mkdir -p "$dir" 2>/dev/null || exit 0
git rev-parse HEAD > "$dir/$sid" 2>/dev/null || true
exit 0
