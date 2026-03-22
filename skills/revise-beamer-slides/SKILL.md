---
name: revise-beamer-slides
description: Use when the user wants to revise an existing Beamer deck in deliverable/slides/, especially by following inline LaTeX comments or instructions, editing specific frames, or turning purpose-and-outline slide stubs into polished Beamer content while preserving the slide purpose as a LaTeX comment.
---

# Revise Beamer Slides

Use this skill when the user already has a Beamer `.tex` file and wants the deck updated in place.

The goal is to make localized, presentation-ready edits inside the existing deck. Start from the slide file itself rather than rebuilding slides from the paper.

## Primary context

For this skill, the target `.tex` file in `deliverable/slides/` is the main working document.

Consult `deliverable/paper/` only when needed to:

- recover notation
- verify a claim or equation
- match the latest project framing

## What to inspect

Inspect only the files needed for the task:

- the target `.tex` file in `deliverable/slides/`
- nearby `%` comments that contain instructions, slide purpose notes, or rough outlines
- older slide decks supplied by the user when they serve as style references
- the most relevant LaTeX draft in `deliverable/paper/` only when needed for notation or factual consistency

## Supported use cases

Use this skill when the user wants to:

- revise existing slides based on inline instructions in the Beamer source
- add a new slide from a purpose comment and a rough outline
- tighten titles, bullets, equations, transitions, or local slide order within an existing deck
- convert rough slide notes into professional Beamer writing without turning them into paper prose

## Comment handling rules

Treat nearby LaTeX comments as authoritative local instructions.

- Keep slide purpose comments as LaTeX comments directly above the relevant frame.
- If the user provides a rough outline for a new slide, preserve the purpose comment and rewrite the outline into polished slide content.
- When a comment is just a scratch instruction, use it to revise the slide and then remove or shorten it unless the user clearly wants it retained.
- When a comment mixes purpose and editing instructions, preserve the purpose and consume the editing instruction.

If a new slide is created from rough notes, prefer a pattern like:

```tex
% Purpose: Explain why the benchmark estimator fails under selective stopping.
\begin{frame}{Selective Stopping Breaks the Benchmark}
    \begin{itemize}
        \item ...
    \end{itemize}
\end{frame}
```

## Workflow

When revising slides:

1. inspect the target Beamer file and locate the relevant frames, comments, and placeholders
2. infer the local editing intent from nearby comments before reading broader project context
3. use the existing deck and any user-provided prior decks as the primary style anchors
4. consult the paper draft only if needed for notation, claims, or terminology
5. rewrite rough outlines into concise, professional slide writing
6. preserve slide purpose comments as LaTeX comments directly above the frame
7. keep edits local and conservative unless the user explicitly asks for a broader reorganization

## Style guide from prior slides

Use the user's prior decks as the default style reference.

When no stronger local style signal is present, prefer the academic Beamer style reflected in the user's examples:

- `\documentclass[10pt]{beamer}`
- `\usetheme{default}` with `\usecolortheme{orchid}`
- black or near-black frametitle text with a thin horizontal rule below it
- square main bullets, circular sub-bullets, and light use of `\vs`
- top-level claims or explanations often appear without bullet icons, while bullets are mainly used for subordinate structure
- concise, formal slide writing rather than manuscript paragraphs

## Editing rules

- Preserve the deck's existing preamble, macros, and frame structure unless the requested edit requires changing them.
- Prefer direct, informative frame titles over vague labels.
- Keep one main message per slide.
- Do not put every sentence in an `itemize` list; when a frame has one main claim plus explanation, prefer a short unbulleted statement, equation, or block.
- Use bullet icons for parallel points or sub-items, and keep such lists short, often two to four items.
- Keep equations only when they are central to the slide's purpose.
- Match notation to the existing deck first, then to the paper if clarification is needed.
- Do not rebuild the whole talk from scratch unless the user explicitly asks.

## Good output standard

A good revision should let the user quickly answer:

- Did the edit follow the inline instruction?
- Is the new slide professional and presentation-ready?
- Is the slide purpose still visible as a LaTeX comment?
- Does the revised frame match the style of the surrounding deck?

Default to targeted, reusable edits rather than a full deck rewrite.

## Boundary with Beamer Slides

Use `beamer-slides` instead when the user wants to create a new deck or initial slide outline from the paper draft.

Use `revise-beamer-slides` when the user already has a deck and wants to work through in-file comments, purpose notes, or rough slide stubs.

## Example prompt patterns

Use this skill when the user asks things like:

- update this `deliverable/slides/main.tex` using my inline comments
- revise these existing slides based on the `% TODO` notes
- add a new slide from the purpose comment and rough outline I left in the file
- rewrite this frame so it sounds more professional but keep the purpose comment
- polish these placeholder bullets inside my current Beamer deck
