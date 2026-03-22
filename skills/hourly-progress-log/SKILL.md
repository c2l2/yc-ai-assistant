---
name: hourly-progress-log
description: Use when the user wants to record hourly progress in meeting-note.md, summarize the most important takeaway from recent work, capture immediate to-dos, or log important but not urgent issues into the backlog.
---

# Hourly Progress Log

Use this skill when the user wants to update the running project log with a short hourly progress entry.

The goal is to preserve momentum and working memory without turning the log into a long diary. Each update should capture the most important takeaway, the next immediate actions, and any important but not urgent issues that belong in the backlog.

## What to inspect

Inspect only the files needed for the task:

- `meeting-note.md`
- `BACKLOG.md`
- the most relevant LaTeX file in `deliverable/paper/` when it helps identify the current project focus
- any rough bullets or discussion from the current chat that should be logged

## Output targets

Default output targets:

- append or revise an hourly progress entry in `meeting-note.md`
- add important but not urgent items to `BACKLOG.md` when appropriate

## Default hourly entry structure

Use this structure unless the user asks for a different format:

```md
## YYYY-MM-DD HH:00

### Key Takeaway

### Immediate To-Dos

### Important but Not Urgent
```

Keep each entry compact and decision-oriented.

## Writing rules

- Focus on the most important takeaway from the past hour, not a full transcript.
- Turn vague next steps into concrete immediate to-dos when possible.
- Move non-urgent but important issues into `BACKLOG.md` rather than burying them in the log.
- Preserve continuity with the current project draft when the work is tied to `deliverable/paper/`.
- Prefer concise bullets over paragraphs.

## Backlog rules

Use `BACKLOG.md` for items that are:

- important for the project
- worth remembering
- not urgent enough to block the current hour's work

When adding backlog items:

- write them as short actionable bullets
- keep them grouped under a simple section if one already exists
- avoid duplicating items that are already present

## Good output standard

A good hourly update should let a future reader quickly answer:

- What mattered most in the last hour?
- What should happen next?
- What important issue should not be forgotten?

## Example prompt patterns

Use this skill when the user asks things like:

- record this hour's progress in `meeting-note.md`
- add an hourly research update
- summarize the key takeaway and next steps from what I just did
- log this issue in the backlog so I do not forget it
- turn this chat into a short progress entry
