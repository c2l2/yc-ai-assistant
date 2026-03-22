---
name: beamer-slides
description: Use when the user wants help turning research notes, paper drafts, theory sketches, or outlines into Beamer slide structure or LaTeX slide content for talks, meetings, or presentations.
---

# Beamer Slides

Use this skill when the user wants to create, revise, or organize slides in LaTeX Beamer format.

The goal is not just to convert text into slides. The goal is to build a presentation that has a clear research narrative, uses the right level of detail, and is easy to paste into an existing Beamer deck.

Match the user's established Beamer style from prior decks whenever possible, both visually and contentwise.

## What to inspect

Inspect only the files needed for the task:

- the most relevant LaTeX file in `deliverable/paper/`, since it contains the latest project framing, notation, and key results
- any outline, pasted text, or rough slide bullets provided by the user

At the slide-making stage, treat the draft paper in `deliverable/paper/` as the primary and usually sufficient source of project content.

## Output targets

Default output is one of the following, depending on the user's request:

- a Beamer slide outline
- LaTeX Beamer frames that can be pasted directly into a deck in `deliverable/slides/`
- a revised talk structure for an existing presentation
- a compact speaking-flow outline for a meeting or workshop talk

## Workflow

When helping with slides:

1. identify the talk purpose, audience, and time constraint if known
2. inspect the most relevant LaTeX draft in `deliverable/paper/` to recover the current project framing
3. extract the smallest set of points needed for a coherent slide narrative
4. organize the presentation into a logical sequence
5. write concise Beamer-ready slide content
6. trim unnecessary detail so each slide has one clear job

## Style guide from prior slides

Use the user's prior slides as the default style reference.

### Visual conventions

- Default to `\documentclass[10pt]{beamer}`.
- Prefer `\usetheme{default}` with `\usecolortheme{orchid}` unless the existing deck clearly uses something else.
- Keep the title and frametitle styling simple and academic rather than decorative.
- Use black or near-black title text and a thin horizontal rule under frame titles when matching the existing deck.
- Prefer standard Beamer bullets with square main bullets and circular sub-bullets when extending an existing deck.
- Keep layouts clean and sparse; avoid flashy visual effects, heavy color, or crowded multi-panel slides unless clearly needed.

### Default preamble conventions

When creating a new Beamer deck or extending a deck that follows the user's usual style, prefer a preamble close to this setup:

```tex
\documentclass[10pt]{beamer}

\mode<presentation> {
\usetheme{default}
\usecolortheme{orchid}
}

\usepackage{setspace}
\usepackage{booktabs,caption}
\captionsetup{justification=centering}
\usepackage[flushleft]{threeparttable}
\usepackage{graphicx}
\usepackage{listings}
\usepackage{mathtools}
\usepackage{bbm}
\usepackage{bm}
\usepackage{amsfonts}
\usepackage{verbatim}
\usepackage{comment}
\usepackage{enumitem}
\usepackage[natbib=true, bibstyle=authoryear, citestyle=authoryear-comp]{biblatex}

\setitemize{label=\usebeamerfont*{itemize item}%
  \usebeamercolor[fg]{itemize item}
  \usebeamertemplate{itemize item}}
\setbeamertemplate{frametitle continuation}[from second][(Cont'd)]
\setbeamertemplate{itemize item}[square]
\setbeamertemplate{itemize subitem}[circle]
\setbeamerfont{itemize/enumerate subbody}{size=\scriptsize}
\setbeamertemplate{bibliography item}{}

\setbeamercolor{lower separation line head}{bg=black}
\setbeamertemplate{frametitle}{
    \vskip0.3cm
    \usebeamerfont*{frametitle}\insertframetitle
    \vskip-0.5ex
    \begin{beamercolorbox}[colsep=0.75pt, wd=\textwidth]{lower separation line head}
    \end{beamercolorbox}
}
\setbeamercolor{title}{fg=black}
\setbeamercolor{frametitle}{fg=black,bg=black!20}
\setbeamercolor{section in head/foot}{bg=black}
\setbeamercolor{author in head/foot}{bg=black}
\setbeamercolor{date in head/foot}{bg=black}

\newcommand{\vs}{\vspace{1em}}
```

Keep the preamble lightweight when possible. Reuse the existing deck preamble if one already exists, and add packages only when the slide content actually needs them.

### Content conventions

- Start from a simple talk arc: motivation, research question, this paper, findings, setup, method, results, limitations, conclusion.
- Use slide titles that are direct and informative, such as `Introduction`, `This Paper`, `Summary of Findings`, `Related Literature`, or a short statement of the main point.
- Prefer short declarative bullets over dense prose.
- Keep one main message per slide.
- Use a small number of bullets, often two to four, rather than long lists.
- Use figures, tables, and equations only when they carry the main point of the slide.
- When presenting technical material, pair formal notation with one sentence of intuition.
- When presenting results, state the substantive conclusion first and put nuance in bullets underneath.

### Beamer writing conventions

- Prefer concise frame content that can be pasted directly into an existing deck.
- Use `\vs` or light vertical spacing when it improves readability and matches the surrounding style.
- Keep notation consistent with the project draft in `deliverable/paper/`.
- Prefer readable tables and centered figures over overloaded slide text.
- Avoid turning slide text into a paragraph copied from the paper draft.

## Slide design rules

- Prefer one clear idea per slide.
- Keep slide text concise and presentation-friendly.
- Use equations only when they are central to the point of the slide.
- Do not paste long paragraphs from the paper draft into slides.
- Emphasize motivation, intuition, identification, main result, and takeaway.
- Keep notation consistent with the LaTeX draft in `deliverable/paper/`.
- Default to Beamer-friendly LaTeX output when the user asks for slide content.
- When extending an existing deck, mirror its package usage and frame structure instead of inventing a new slide style.

## Good output standard

A good slide draft should let a future presenter quickly answer:

- What is the main message of the talk?
- Why does each slide exist?
- What is the audience supposed to remember?
- Which technical details are essential and which can be omitted?

Default to concise output: enough detail to build a deck, but not so much that the slides become a second paper.

## Example prompt patterns

Use this skill when the user asks things like:

- turn this draft into Beamer slides
- make slides for this theory section
- outline a seminar talk from my paper draft
- convert these notes into presentation frames
- shorten these slides for a meeting presentation
- add a few slides to my existing Beamer deck based on this discussion
- revise these existing slides using the points we just discussed
- add a transition slide between these two sections
- insert a new result slide into my current presentation
- update this deck to reflect the latest draft or meeting discussion
