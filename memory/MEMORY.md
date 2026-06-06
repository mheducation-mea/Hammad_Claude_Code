# MEMORY — index

> Read this first. It points to every memory file by purpose.
> Memory here is deliberate, not automatic. Update it at the end of any substantive session.
> Where this repo and Notion disagree, Notion wins, then update here.

## Files

| File | Holds | When to read |
|---|---|---|
| `notion-marketing-ops-source-of-truth.md` | The full Notion build: model, architecture decisions, every database ID, conventions, MCP/API learnings, backlog. Hammad's living reference. | Before any Notion work |
| `decisions-and-learnings.md` | Durable decisions, rules learned, and project state captured during Claude Code sessions. | Before starting work; append at session end |

## Write-back rule

At the end of a substantive session:
1. Add new decisions, rules, or state to `decisions-and-learnings.md` (newest at top).
2. If a global rule changed, update `../CLAUDE.md`.
3. If the Notion architecture changed, update `notion-marketing-ops-source-of-truth.md` (and remember Notion itself is the system of record).
