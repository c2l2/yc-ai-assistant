# Internal Codex Implementation Record

This file tracks changes to the AI workflow itself. It is not a team-management
record. Team assignments and task history live entirely in finalized weekly
meeting notes.

## Status Legend

- `todo`
- `in_progress`
- `blocked`
- `done`

## Active Sequence

| ID | Status | Task | Output / Deliverable | Notes |
| --- | --- | --- | --- | --- |
| T1 | done | Replace the deterministic workflow design with the manager-led weekly process. | Repository workflow documentation | Remove the planned workflow script and tests. |
| T2 | done | Create root context, current-state documents, and the English weekly template. | Root Markdown files and `templates/weekly-meeting.md` | Team members write their own updates. |
| T3 | done | Create separate review and finalization skills. | `skills/review-weekly-progress/` and `skills/finalize-weekly-meeting/` | Review is read-only; finalization is manager-invoked. |
| T4 | done | Retire conflicting paths and validate the redesigned workflow. | Clean file map and validation results | No old running-note or automated weekly-workflow path remains active. |
| T5 | done | Retire the separate Codex session handoff. | Removed session file and updated repository instructions | Its former runner dependency was removed before the runner itself was retired in T6. |
| T6 | done | Retire the internal Codex task runner. | Remove the runner, its Makefile targets, and active references | The internal task record is manual and cannot launch Codex. |
| T7 | done | Retire the root team task register. | Store current assignments in finalized weekly notes | `Next Actions` is now the complete current task snapshot. |
| T8 | done | Generalize the repository agent instructions. | Synchronized root and assistant `AGENTS.md` files | Research, empirical, and software workflows are primary; weekly coordination is optional. |
| T9 | done | Treat weekly meeting files as internal manager reports. | Updated template, skills, and workflow documentation | Reports remain flat under `report/` with the manager as primary audience. |
| T10 | done | Split Beamer initialization and revision into separate skills. | `skills/beamer-slides/SKILL.md`, `skills/revise-beamer-slides/SKILL.md` | New decks start from paper context; existing decks use the target file and inline comments. |
| T11 | done | Add frame-level message and source-navigation conventions. | Beamer initialization and revision skills | Use `% message:` comments and place `% -----------------` between generated frames. |
| T12 | done | Avoid math-first slide bodies. | Beamer initialization and revision skills | Lead with a short verbal setup before a displayed equation when possible. |
| T13 | done | Keep figure and table slides sparse. | Beamer initialization and revision skills | Use takeaway titles, at most two visible sentences, and presenter-note comments. |
| T14 | done | Avoid one-word or two-word trailing lines. | Beamer initialization and revision skills | Shorten or rephrase awkwardly wrapped sentences. |
| T15 | done | Make revised frames auditable. | `skills/revise-beamer-slides/SKILL.md` | Add `%revised` and report the first revised frame line. |
| T16 | done | Protect unsaved Beamer editor changes. | `skills/revise-beamer-slides/SKILL.md` | Stop and ask the user to save when the on-disk file may be stale. |

## Task Template

```md
### T#

- Status: `todo`
- Goal:
- Inputs:
- Target files:
- Definition of done:
- Depends on:
- Notes for Codex:
```
