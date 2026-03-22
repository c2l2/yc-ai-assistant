---
name: letter-to-editor
description: Use when the user wants to draft, revise, shorten, or polish a letter to the editor or confidential comments to the editor based on the paper under review, the draft referee report, and additional comments provided in chat.
---

# Letter To Editor

Use this skill when preparing editor-facing review text such as a letter to the editor, confidential comments to the editor, or an editor-only recommendation note.

The goal is to produce a concise, candid, professionally toned letter that synthesizes three sources:

- the paper itself
- the draft referee report
- additional comments or recommendation cues provided by the user in chat

This skill is for editor-facing communication, not the author-facing report. The letter should therefore be more synthesis-heavy, recommendation-aware, and explicit about overall fit, severity of concerns, and revision prospects.

## What to inspect

Inspect only the files needed for the task:

- the paper-specific folder under `report/`; treat each folder as one review unit
- the target paper PDF, manuscript, slides, abstract, or excerpt inside that folder
- the latest draft referee report inside that same folder
- the user's additional comments in chat; treat these as primary input when they concern recommendation, fit, hidden concerns, or editor-only nuance
- any review form fields that distinguish author comments from editor comments
- other local notes only when the user explicitly wants cross-reference or comparison

## Default output

Always do both:

- write the editor letter as a Markdown file inside the paper's folder under `report/`
- return the same letter as plain text in chat

Treat `report/<paper-folder>/` as the default working directory for that review task.

Filename pattern:

- `YYYY-MM-DD-<journal>-<keywords>-letter-to-editor.md`

Examples:

- `report/llm-epu/2026-03-20-jbf-llm-epu-letter-to-editor.md`
- `report/qte-fiscal-rules/2026-03-20-tea-qte-fiscal-rules-letter-to-editor.md`

Filename rules:

- use the current date in `YYYY-MM-DD`
- use a short journal slug or abbreviation
- use 2 to 5 short keyword slugs that identify the paper
- keep the filename ASCII and hyphen-separated
- if the journal is unclear, use `unknown-journal`

## Core workflow

1. Read the paper to recover the main question, method, evidence, and contribution.
2. Read the draft referee report and treat it as the main source for the public-facing evaluation already given to the author.
3. Incorporate any additional comments from the user in chat, especially when they concern recommendation strength, journal fit, credibility, hidden reservations, or editor-only context.
4. Make sure the editor letter is consistent with the draft report in substance, unless the user explicitly wants a stronger private signal to the editor.
5. State the overall recommendation or bottom line clearly when the form or user request calls for it.
6. Explain briefly why the paper is or is not ready, which concerns are central, and whether the issues seem addressable in revision.
7. Save the letter as a Markdown file in the same `report/<paper-folder>/` directory and then return a plain-text version in chat.

If the user provides chat bullets or outline comments, preserve their substantive points and relative priority, then rewrite them into polished editor-facing prose.

## Style and stance

- Default to professional academic English unless the user asks for another language.
- Be concise. This is usually shorter and more synthesis-heavy than the author-facing referee report.
- Be candid but fair. Do not soften important concerns into vagueness.
- Focus on what the editor most needs to know: contribution, fit, seriousness of concerns, and likely revision path.
- Avoid repeating the full public report point by point.
- When appropriate, distinguish between concerns that are likely fixable and concerns that threaten publishability.
- If the user signals editor-only reservations in chat, include them carefully and directly.
- Keep the tone collegial and evidence-based rather than emotional or adversarial.

## What the editor letter should do

A strong editor letter usually covers:

- what the paper is trying to contribute
- whether the contribution is potentially interesting for the journal
- whether the current draft is convincing
- which concerns are most important
- whether the concerns appear fixable in a normal revision cycle
- what recommendation follows from that assessment

## Default structure

Use this structure unless the journal form requires a different one:

```md
Dear Editor,

Thank you for the opportunity to review this manuscript. The paper studies ...

Overall, I view the paper as ...

My recommendation is based mainly on the following considerations:

1. Main consideration
2. Main consideration
3. Main consideration

If the paper is invited for revision, the most important issues to address would be ...
```

If the form asks specifically for confidential comments to the editor, adapt the format to the form rather than forcing a letter opening.

## Writing rules

- Base the letter on both the paper and the draft referee report.
- Treat the chat comments as important supplementary input, especially when they contain editor-only judgments or recommendation cues.
- Do not contradict the public report unless the user explicitly wants to signal a stronger private recommendation.
- Do not invent facts, references, or concerns not supported by the paper, report, or user comments.
- Do not copy the referee report wholesale; compress and synthesize.
- If the user gives a recommendation such as reject, major revision, minor revision, or accept, preserve that recommendation unless there is clear instruction to reconsider it.
- When the recommendation is mixed, explain the tradeoff directly.
- Keep confidential comments appropriate for the editor and avoid gratuitous speculation about the authors.

## Journal-form adaptation

If the user provides a review form with fields such as recommendation, confidential comments to the editor, comments to the authors, or suitability for the journal:

- answer the editor-only field directly
- keep the editor-facing note distinct from the author-facing report
- state the recommendation clearly if the form asks for it
- mention journal fit when that is part of the editorial decision

## Good output standard

A good editor letter should let the editor quickly understand:

- what the paper contributes
- how strong the paper currently is
- what the most important concerns are
- whether those concerns are fixable
- what recommendation the referee is implicitly or explicitly making

Default to medium detail: specific enough to guide an editorial decision, short enough to read in one pass.

## Example prompt patterns

Use this skill when the user asks things like:

- write the letter to the editor for this paper
- draft confidential comments to the editor based on my report
- use the paper and my draft referee report to write an editor letter
- I will add extra editor-only comments in chat; incorporate them into the letter
- shorten these confidential comments to the editor
- make the editor letter more direct about my recommendation
