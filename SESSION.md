# Current Session State

Use this file as the handoff note between separate Codex prompts.

## Current Objective

- Keep the Beamer slide skills aligned with the user's slide-authoring conventions as the user provides incremental updates.

## Current Task

- Task ID: T8
- Status: `done`

## Relevant Files

- `skills/beamer-slides/SKILL.md`
- `skills/revise-beamer-slides/SKILL.md`
- `TASKS.md`
- `SESSION.md`

## Latest Decisions

- In `beamer-slides`, every newly generated frame should include a `% message:` comment stating the slide's intended takeaway.
- In `revise-beamer-slides`, `% message:` comments should be read as authoritative frame-level intent alongside `GPT-*` tags and `%GPT:` comments.
- `% message:` comments should stay concise and be placed near the top of the frame.
- Both skills should discourage slides whose first visible body content is a standalone displayed equation.
- When math is needed, slides should usually begin with a short verbal setup, claim, or intuition line before the equation.
- On slides centered on figures or tables, the visible frame text should usually be at most two sentences.
- For result-heavy figure/table slides, the takeaway can live in the frame title rather than in a long on-slide paragraph.
- Fuller speaking guidance for result slides should go into LaTeX `% presenter notes:` comments inside the frame.
- Slides should avoid wrapped sentences whose last line contains only one or two words.
- When that happens, the sentence should be shortened or rephrased rather than left as-is.

## Files Changed This Turn

- `skills/beamer-slides/SKILL.md`
- `skills/revise-beamer-slides/SKILL.md`
- `TASKS.md`
- `SESSION.md`

## Open Blockers

- None.

## Recommended Next Prompt

`Please apply the next Beamer skill instruction.`
