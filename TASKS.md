# Task Queue

Use this file when the work is intentionally split across multiple prompts.

## How To Use

- Keep tasks small enough that Codex can finish one in a single turn.
- Put tasks in the order you want Codex to attempt them.
- Mark exactly one task as `in_progress` at a time.
- Move important but deferrable ideas to `BACKLOG.md`.
- At the end of each turn, update statuses and note the next recommended prompt in `SESSION.md`.

## Status Legend

- `todo`
- `in_progress`
- `blocked`
- `done`

## Active Sequence

| ID | Status | Task | Output / Deliverable | Notes |
| --- | --- | --- | --- | --- |
| T1 | done | Add a one-sentence purpose statement to `toy-demo.md`. | `toy-demo.md` | Keep it to one short sentence under a new `## Purpose` heading. |
| T2 | done | Add a three-item numbered checklist to `toy-demo.md`. | `toy-demo.md` | Put it under a new `## Checklist` heading. |
| T3 | done | Add a final completion note to `toy-demo.md`. | `toy-demo.md` | Add a `## Completion Note` heading with one short paragraph. |
| T4 | done | Update Beamer slide skills to support `% message:` comments for frame-level slide intent. | `skills/beamer-slides/SKILL.md`, `skills/revise-beamer-slides/SKILL.md` | New slides should add `% message:` comments; revisions should read them as the intended takeaway. |
| T5 | done | Commit and push the current Beamer skill updates. | Git commit on `main` and push to `origin`. | Include the skill changes and handoff-note updates from this turn. |

## Task Template

Copy this block when you need more detail for a task:

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

## Toy Demo Notes

You can test the automation with:

```bash
make codex-task-next
make codex-task-next
make codex-task-next
```

Expected result:

- `toy-demo.md` is updated in three small steps
- `TASKS.md` moves from `todo` to `done`
- `SESSION.md` keeps the handoff current after each run
