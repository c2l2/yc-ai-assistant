---
name: english-referee-report
description: Use when the user wants to draft, revise, shorten, or polish an English referee report based on a paper PDF, manuscript, slides, or an outline of major and minor comments provided in chat.
---

# English Referee Report

Use this skill when preparing an academic referee report in English.

The goal is to produce a concise, fair, technically grounded author-facing report: start with a faithful summary of the paper, give a balanced overall assessment, then organize comments into clear major and minor points with actionable suggestions.

## What to inspect

Inspect only the files needed for the task:

- the paper-specific folder under `report/`; treat each folder as one review unit
- the target paper PDF, manuscript, slides, abstract, or excerpt inside that folder
- the user's chat outline of major comments and minor comments; treat this as primary input when provided
- any rough bullets, prior draft comments, or review form fields supplied by the user
- directly relevant local references only when needed to confirm terminology or method comparisons
- other local notes only when the user explicitly wants cross-reference or comparison

## Default output

Always do both:

- write the draft report as a Markdown file inside the paper's folder under `report/`
- return the same report as plain text in chat

Treat `report/<paper-folder>/` as the default working directory for that review task.

Filename pattern:

- `YYYY-MM-DD-<journal>-<keywords>-report-en.md`

Examples:

- `report/llm-epu/2026-03-20-jbf-llm-epu-report-en.md`
- `report/qte-fiscal-rules/2026-03-20-tea-qte-fiscal-rules-report-en.md`

Filename rules:

- use the current date in `YYYY-MM-DD`
- use a short journal slug or abbreviation
- use 2 to 5 short keyword slugs that identify the paper
- keep the filename ASCII and hyphen-separated
- if the journal is unclear, use `unknown-journal`

## Core workflow

1. Recover the paper's main question, method, data or theoretical setup, and headline findings.
2. If the user provides a chat outline of major and minor comments, use that outline as the backbone of the report.
3. Open with one concise paragraph summarizing the paper's contribution and core result.
4. Add one short overall assessment paragraph when appropriate, especially if the paper has clear strengths, novelty, or publication potential.
5. Organize the rest into `Major Comments` and `Minor Comments`.
6. For each major comment, provide:
   - a short issue label
   - why the issue matters
   - a concrete suggestion, clarification request, or possible extension
7. Use minor comments for precision issues such as exposition, terminology, references, figures, notation, or likely typos.
8. Save the report as a Markdown file in the same `report/<paper-folder>/` directory and then return a plain-text version in chat.

If the user provides rough bullets or an outline of major and minor comments in chat, preserve their substantive points and relative priority, then rewrite them into polished, coherent prose.

## Style and stance

- Write in professional academic English.
- Begin with a neutral, accurate summary before moving into criticism.
- Be constructive and respectful. The report should help the author understand how the paper can improve.
- Acknowledge strengths explicitly when warranted, especially clarity of structure, completeness of analysis, robustness checks, or practical contribution.
- Use concrete, technically meaningful suggestions rather than vague approval or dismissal.
- Keep the report compact. A strong default is roughly 1 to 2 pages unless the user asks for a longer form.
- Avoid exaggerated certainty. If a concern is tentative, frame it as a question, a request for clarification, or a suggestion for discussion.

## Comment patterns

Common strong major comments include:

- the paper motivates a method but does not define its core object clearly enough
- multiple estimators are compared, but the paper does not explain which one should be treated as the main specification
- an identifying assumption is used but not stated sharply
- a robustness or extension is natural and would sharpen the contribution
- descriptive evidence is shown, but its link to the research question is not yet explained
- model design choices are under-justified

Common strong minor comments include:

- terminology is imprecise
- a reference is missing, incorrect, or inconsistently cited
- a figure axis, unit, table label, or notation is unclear
- a title does not fully reflect the paper's true focus
- a sentence likely contains a typo or mislabeling

## Default structure

Use this structure unless the user asks for a different format or provides a journal-specific review form:

```md
This paper studies ...

Overall, the paper's main strengths are ..., while the main concerns are ...

Major Comments:
1. Titled major comment
Explain what the issue is, why it matters, and how the authors could address it.

2. Titled major comment
Subpoints may be added if needed.

Minor Comments:
1. Short, precise writing, terminology, figure, or citation suggestion
2. Short, precise writing, terminology, figure, or citation suggestion
```

## Writing rules

- Separate paper summary from evaluation.
- Do not invent strengths, weaknesses, results, or references that are not supported by the manuscript or user notes.
- Keep major comments limited and prioritized. Usually 2 to 4 major comments are enough.
- Make each major comment self-contained so the author can respond to it directly.
- Prefer actionable suggestions over purely negative statements.
- When the user supplies major and minor comments as an outline in chat, preserve that structure unless there is a strong reason to merge, reorder, or split points.
- Preserve the paper's own notation and terminology unless the point of the comment is that the notation or terminology is misleading.
- When the paper is promising but incomplete, say so directly and then specify what would raise confidence.
- When the paper is strong overall, allow the positive assessment to appear explicitly before the critique.
- When the user asks for a stronger or harsher report, increase directness but keep the language professional and evidence-based.
- The saved `.md` file and the chat reply should contain the same substantive report.
- In chat, present the report as plain text rather than only summarizing what was written to the file.

## Journal-form adaptation

If the user provides a review form with fields such as contribution, originality, validity, recommendation, or confidential comments to the editor:

- answer each field directly rather than forcing everything into free-form prose
- keep the public report constructive and author-facing
- keep editor-only comments clearly separated if the form requires them
- do not state an accept or reject recommendation in the author-facing text unless the user explicitly wants that style

## Good output standard

A good report in this style should let the author quickly understand:

- what the referee thinks the paper is trying to contribute
- what the paper is already doing well
- which issues are most important
- which fixes are clarifications versus substantive extensions
- how to revise the paper without guessing what the referee meant

Default to medium detail: specific enough to be useful in revision, short enough to read in one pass.

## Example prompt patterns

Use this skill when the user asks things like:

- write an English referee report for this paper
- based on this paper and my notes, draft the referee report in English
- I will give you major comments and minor comments in chat; turn them into a formal English referee report
- rewrite these referee-report bullets into polished English
- shorten this referee report in English but keep the major and minor comments
- make the tone more diplomatic without making the comments vague
