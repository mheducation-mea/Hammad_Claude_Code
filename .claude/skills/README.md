# Marketing Skill Set — McGraw Hill K-12 International

A composed set of three Claude Code skills, ported from Hammad Khilji's original
Claude.ai skills. Each skill is kept separate (its own directory + `SKILL.md`) and
auto-invokes from the `description` in its frontmatter. They are designed to work
together.

## The skills

| Skill | Purpose | Depends on |
|---|---|---|
| `hammad-b2b-copywriting` | Foundation. The voice and review standards for all customer-facing copy: benefit-first, you-phrasing, no hedging, no jargon, one CTA, no em dashes. | None. Base layer. |
| `email-nurture-campaign-builder` | 6-phase engine for B2B nurture sequences for educational products: discovery, planning table, generation, QA. | `hammad-b2b-copywriting` |
| `international-school-profiler` | ABM intelligence: 16-section, 3,500-5,000 word profiles of international schools. | `WebSearch`, `WebFetch` |

## How they compose

```
hammad-b2b-copywriting  (voice + standards, the constant)
        ▲
        │ applied to every email
        │
email-nurture-campaign-builder      international-school-profiler
   (uses copywriting standards)        (standalone; needs web tools)
```

When `email-nurture-campaign-builder` runs, it loads `hammad-b2b-copywriting` and
applies those standards to every email. On any conflict, the copywriting rules win.

## Notes on the port

- Frontmatter was normalised to the Claude Code standard (`name` + `description`).
  Original metadata (version, tags) is preserved as a comment inside each `SKILL.md`.
- `international-school-profiler` tool references were updated to Claude Code's
  `WebSearch` and `WebFetch` tools.
- Content is otherwise unchanged from the originals.
