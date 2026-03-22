---
name: chinese-referee-report
description: Use when the user wants to draft, revise, shorten, or polish a Chinese referee report, 審查意見, or 審查報告 in Traditional Chinese based on a paper PDF, manuscript, slides, or an outline of major and minor comments provided in chat.
---

# Chinese Referee Report

Use this skill when preparing an academic referee report in Traditional Chinese.

The goal is to produce a concise, fair, technically grounded report in the user's established style: start with a faithful summary of the paper, give a balanced overall assessment, then organize comments into clear major and minor points with actionable suggestions.

## What to inspect

Inspect only the files needed for the task:

- the paper-specific folder under `report/`; treat each folder as one review unit
- the target paper PDF, manuscript, slides, abstract, or excerpt inside that folder
- the user's chat outline of `主要評論` and `次要評論`; treat this as primary input when provided
- any rough bullets, prior draft comments, or review form fields supplied by the user
- directly relevant local references only when needed to confirm terminology or method comparisons
- other local notes only when the user explicitly wants cross-reference or comparison

## Default output

Always do both:

- write the draft report as a Markdown file inside the paper's folder under `report/`
- return the same report as plain text in chat

Treat `report/<paper-folder>/` as the default working directory for that review task.

Filename pattern:

- `YYYY-MM-DD-<journal>-<keywords>.md`

Examples:

- `report/llm-epu/2026-03-20-jbf-llm-epu-keywords.md`
- `report/qte-fiscal-rules/2026-03-20-tea-qte-fiscal-rules.md`

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
5. Organize the rest into `主要評論` and `次要評論`.
6. For each major comment, provide:
   - a short issue label
   - why the issue matters
   - a concrete suggestion, clarification request, or possible extension
7. Use minor comments for precision issues such as exposition, terminology, references, figures, notation, or likely typos.
8. Save the report as a Markdown file in the same `report/<paper-folder>/` directory and then return a plain-text version in chat.

If the user provides rough bullets or an outline of major and minor comments in chat, preserve their substantive points and relative priority, then rewrite them into polished, coherent prose.

## House style from the user's examples

- Write in Traditional Chinese using a professional Taiwan academic tone.
- Begin with a neutral, accurate summary before moving into criticism.
- Be constructive and respectful. The stance is "this paper has value, and here is how to strengthen it," not adversarial fault-finding.
- Acknowledge strengths explicitly when warranted, especially clarity of structure, completeness of analysis, robustness checks, or practical contribution.
- Use concrete, technically meaningful suggestions rather than vague approval or dismissal.
- Prefer formulations such as `本文...`, `作者...`, `整體而言...`, `本人認為...`, `建議作者...`, `讀者可能...`.
- On first mention of specialized methods or concepts, optionally include the English term in parentheses when it helps precision.
- Keep the report compact. A strong default is roughly 1 to 2 pages in Chinese unless the user asks for a longer form.
- Avoid exaggerated certainty. If a concern is tentative, frame it as a question, a request for clarification, or a suggestion for discussion.

## Comment patterns that fit this style

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
本文先以 1 段說明研究問題、方法與主要結果。

整體而言，以 1 段概括文章優點、完整度與主要保留意見。

主要評論：
1. 標題式主評論
說明問題何在、為何重要，以及建議作者如何補強。

2. 標題式主評論
必要時可加上：
a. 子建議

次要評論：
1. 精確但簡短的寫作、術語、圖表或引用建議
2. 精確但簡短的寫作、術語、圖表或引用建議
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

- 幫我寫這篇的中文審查意見
- 根據這篇論文和我的筆記，整理成 referee report
- 我會在 chat 給你 major comments 和 minor comments 的 outline，請幫我整理成正式審查意見
- 把我這些 review bullets 改寫成正式的中文審查報告
- 幫我把英文 referee comments 改成中文、保留學術口吻
- 幫我縮短這份審查意見，但保留主要評論與次要評論
- 幫我把語氣改得更委婉一點，但意見不要變空泛
