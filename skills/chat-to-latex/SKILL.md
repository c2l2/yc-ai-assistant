---
name: chat-to-latex
description: Use only when the user explicitly asks to integrate the current discussion, notes, or outlines into the paper draft in deliverable/paper/. Before integration, present the proposed LaTeX additions in chat for review and check notation consistency against the paper draft.
---

# Chat to LaTeX

Use this skill only when the user explicitly asks to integrate ongoing discussion or research notes into the paper draft.

The goal is not just to rewrite notes in LaTeX syntax. The goal is to produce manuscript-ready text that fits the current draft, preserves the intended argument, and reads like part of a paper rather than a note dump.

## What to inspect

Inspect only the files needed for the task:

- the most relevant LaTeX draft in `deliverable/paper/`
- relevant Markdown notes in `references/`
- relevant meeting-note or backlog context only when it materially affects framing
- any outline, section draft, or pasted text provided by the user

Treat the LaTeX draft in `deliverable/paper/` as the primary anchor for notation, tone, structure, and local context.

## Output targets

Default output is one of the following, depending on the user's request:

- LaTeX paragraphs that can be pasted directly into the paper draft
- a subsection or section draft in LaTeX
- a rewritten version of rough notes in paper prose
- a bridge paragraph or transition connecting existing draft sections

## Workflow

When converting discussion or notes into LaTeX:

1. inspect the relevant manuscript draft in `deliverable/paper/`
2. identify the target section, audience, and purpose of the requested text
3. extract the stable ideas from the discussion or notes and ignore brainstorming debris unless the user wants it preserved
4. check notation, terminology, and symbol definitions against the current paper draft
5. organize the material into a paper-friendly sequence
6. write concise LaTeX-ready prose
7. show the proposed addition in chat before integrating it into the paper

## Writing rules

- Preserve the intended claim, but rewrite for paper readability.
- Match the notation and terminology already used in `deliverable/paper/`.
- Explicitly check notation consistency with the paper before proposing text for integration.
- Do not present speculative ideas as finalized claims.
- Prefer clean prose over literal note-to-sentence translation.
- Keep citations aligned with the surrounding draft when relevant.
- When the notes are still exploratory, say so and avoid over-polishing them into false certainty.
- Use LaTeX formatting only where it helps integrate the text into the draft.
- Before integrating, present the exact proposed LaTeX text in chat so the user can review what will be added.

## Boundary with Theory Workbench

Use `theory-workbench` when the argument is still being developed, tested, or debugged.

Use `chat-to-latex` when the argument is stable enough that the main need is writing it clearly into the paper draft or incrementally adding new text during the project.

## Good output standard

A good output should let the user quickly paste the text into the draft with minimal cleanup and answer:

- Does this sound like part of the paper?
- Is the notation consistent?
- Is the argument clearer than in the original notes?
- Does the paragraph fit the surrounding section?

Default to concise manuscript prose rather than long explanatory notes.

## Example prompt patterns

Use this skill when the user asks things like:

- turn these notes into a LaTeX subsection
- rewrite this outline as paper prose
- draft a paragraph for my identification section
- convert these theory notes into manuscript text
- write a transition between these two sections
- adapt this Markdown note for the paper draft
- add a new paragraph to my LaTeX draft based on this discussion
- turn this chat into text I can paste into the paper
- expand this section of the draft using the points we just discussed
