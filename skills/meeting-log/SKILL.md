---
name: meeting-log
description: Use when the user wants to summarize a meeting, clean up meeting-note.md, extract action items or open questions, or turn rough discussion notes into a reusable Markdown research log.
---

# Meeting Log

Use this skill when working on `meeting-note.md` or when the user provides rough meeting notes that should become a clean Markdown summary.

The goal is to keep meeting notes useful as long-term research memory. A good meeting note should be easy to scan later, preserve important decisions, and make follow-up work obvious.

Use the user's established meeting format in English. Preserve the structure and intent of the older Google Doc format rather than replacing it with a generic note style.

## What to inspect

Inspect only the files needed for the task:

- `meeting-note.md`
- any rough bullets, pasted notes, or transcript excerpts provided by the user
- images in `attachments/meetings/` if they are referenced
- related local notes in `references/` or other Markdown files only when they are needed for context
- the most relevant LaTeX file in `deliverable/paper/` when it helps recover the latest project context

## Output location

Default output target:

`meeting-note.md`

If the user asks for a separate note, keep the same structure and use a descriptive Markdown filename.

## Figure handling

If the meeting note includes pasted figures or whiteboard images, store them under:

`attachments/meetings/`

Use relative links from `meeting-note.md`.

Example:

```md
![Whiteboard sketch](./attachments/meetings/2026-03-14-proof-outline.png)
```

Do not create or move figures unless the task requires it. Prefer reusing existing attached files.

## Default note structure

Use this structure unless the user asks for a different format or the existing note already uses a stable structure.

```md
# Meeting Notes

Date: YYYY-MM-DD

## Meeting Goals / Agenda

- Review progress
- Clarify and resolve current blockers
- Discuss next actions and division of labor

## Key Takeaways

## Consensus and Decisions

## Next Actions

## Unresolved Questions

## Other
```

If a section is not useful for the current meeting, omit it instead of filling it with weak content.

## Writing rules

- Keep the note concise and easy to scan.
- Add the meeting date near the top using `YYYY-MM-DD`.
- Keep the agenda focused on the user's standard three meeting purposes unless the user provides a different agenda.
- Distinguish clearly between decisions, ideas, and unresolved questions.
- Preserve the user's original wording when it contains important nuance.
- Turn vague follow-up tasks into concrete next actions when possible.
- When the note mentions post-meeting execution, make it explicit that follow-up issues should be opened after the meeting.
- Keep open questions visible rather than burying them inside long prose.
- Put important progress summaries and research findings in `Key Takeaways`.
- Put timing, direction, and agreed plans in `Consensus and Decisions`.
- Put ownership and concrete follow-up work in `Next Actions`.
- Use `Other` only for points that do not fit naturally elsewhere.

## Update behavior

When updating an existing meeting note:

- preserve the existing filename and broad structure unless the user asks for a rewrite
- retain the user's original comments when they capture important context
- remove duplication if the note became repetitive
- preserve relative links to local attachments when they already exist
- keep the note readable as a running log rather than a one-time transcript

## Good output standard

A good meeting note should let a future reader quickly answer:

- What was the purpose of the meeting?
- What decisions were made?
- What follow-up work is needed?
- What questions remain open?
- What progress or findings mattered most?

Default to medium detail: detailed enough to preserve research context, short enough to skim quickly.

## Example prompt patterns

Use this skill when the user asks things like:

- summarize this meeting into `meeting-note.md`
- clean up these rough meeting bullets
- extract action items from this discussion
- update the meeting note with these new points
- turn this meeting transcript into a structured research log
