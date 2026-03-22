# AGENTS.md

## Repo Purpose

This repository is a research workspace for theory-heavy work in econometrics,
statistics, and related fields.

The repo is designed so that:
- Markdown stores the working research memory
- LaTeX in `deliverable/paper/` stores the evolving formal draft
- slides in `deliverable/slides/` are derived from the paper draft
- Codex can read local files and help across the full research workflow

## Global Interpretation Rules

- Treat Markdown as the canonical research memory.
- Treat the most relevant LaTeX file in `deliverable/paper/` as the main source
  of current project context whenever the task touches the paper, theory, or
  slides.
- Treat `deliverable/slides/` as a presentation layer derived from the paper
  draft, not as the main place to develop ideas.
- Prefer local repo context over unsupported assumptions.

## Folder Meaning

- `meeting-note.md`: running meeting log and project coordination memory
- `BACKLOG.md`: important but not urgent items that should not be forgotten
- `references/`: paper PDFs and Markdown reading notes
- `attachments/meetings/`: images for meeting notes
- `attachments/references/`: images for reading notes
- `data/`: raw, processed, temporary, and code-related data work
- `finding/`: empirical work, simulation, and intermediate research outputs
- `report/`: Markdown files that mainly link to external files or reporting artifacts
- `deliverable/paper/`: main paper draft and manuscript files
- `deliverable/slides/`: Beamer slides and presentation files
- `templates/`: reusable templates
- `skills/`: task-specific Codex skills

## Context Priority

When building context, prioritize files in this order when relevant:

1. the most relevant file in `deliverable/paper/`
2. directly relevant files in `references/`
3. `meeting-note.md`
4. directly relevant files in `finding/`
5. templates only when creating new artifacts

Do not read broadly without need. Prefer targeted inspection.

## Workflow Conventions

- Use structured Markdown notes so ideas remain reusable.
- Use relative links for Markdown images.
- Keep paper-note images in `attachments/references/`.
- Keep meeting-note images in `attachments/meetings/`.
- Use `TASKS.md` as the queue for multi-step work that will be handled across
  separate prompts.
- Use `SESSION.md` as the active handoff note between Codex turns.
- Use R by default for simulation work unless the project clearly uses another language.
- Match notation to the existing LaTeX draft before adding manuscript text.
- Only integrate current chat into `deliverable/paper/` when the user explicitly asks.
- Before integrating text into the paper, show the proposed LaTeX in chat first.
- For literature search, prioritize stronger journals, especially in economics,
  econometrics, and the user's preferred management-science subfields.
- For slides, match the user's established Beamer style when possible.

## Skill Usage

Use repo-local skills when the task matches them:

- `paper-note`
- `meeting-log`
- `hourly-progress-log`
- `theory-workbench`
- `paper-search`
- `simulation-runner`
- `beamer-slides`
- `chat-to-latex`
- `chinese-referee-report`
- `english-referee-report`
- `letter-to-editor`

Skills provide task-specific rules. This file provides global repo-level rules.

## Output Philosophy

- Help with structuring, critique, synthesis, writing, and continuity.
- Do not over-polish exploratory ideas into false certainty.
- Be explicit about uncertainty, assumptions, and gaps.
- Prefer concise, reusable outputs over long generic prose.

## Sequential Prompt Protocol

When the user wants Codex to work through a sequence of tasks using separate
prompts, follow this protocol:

1. Read `TASKS.md` and `SESSION.md` first if they exist and are relevant.
2. Work on one scoped task at a time unless the user explicitly asks to batch.
3. Update the task status in `TASKS.md` when a task starts or finishes.
4. Leave a short handoff in `SESSION.md` with:
   - current objective
   - files changed or created
   - decisions made
   - unresolved blockers
   - the single best next prompt for the next turn
5. Prefer passing context through local files instead of relying on long chat history.

This repo is optimized for prompt-chained work: plan in `TASKS.md`, execute one
task per turn, and preserve continuity in `SESSION.md`.

If the repo-local automation exists, it may invoke Codex through `make
codex-task-next` or `make codex-task-resume` instead of manual prompt entry.
