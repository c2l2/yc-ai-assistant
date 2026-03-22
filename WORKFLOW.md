# Research Workflow

This repository uses Markdown as the canonical research memory.

The workflow is designed so that notes stay local and readable by Codex, while
the paper draft in `deliverable/paper/` becomes the main formal output over
time.

## Core Principles

- Markdown files store the working research memory.
- The most relevant LaTeX draft in `deliverable/paper/` usually contains the latest project context.
- Slides in `deliverable/slides/` should be derived from the paper draft rather than from scattered notes.
- Skills are used to support repeated workflows, not to replace the repo structure.
- Separate prompts are a feature, not a limitation: use local task and handoff files to preserve context across turns.

## Folder Roles

- `meeting-note.md`: running meeting summary and research coordination log
- `BACKLOG.md`: important but not urgent issues and follow-ups
- `TASKS.md`: queue of scoped tasks for multi-turn Codex execution
- `SESSION.md`: active handoff note for the next Codex prompt
- `references/`: paper PDFs and corresponding Markdown notes
- `attachments/meetings/`: images used by meeting notes
- `attachments/references/`: images used by paper notes
- `data/`: raw, processed, temporary, and code-related data work
- `finding/`: empirical analysis, modeling, and simulation work
- `report/`: Markdown files that point to external docs or reporting artifacts
- `deliverable/paper/`: main paper draft and manuscript files
- `deliverable/slides/`: Beamer slide decks and slide-related files
- `templates/`: reusable templates for analysis and simulation
- `skills/`: Codex workflow skills for repeated research tasks

## Research Pipeline

Typical project flow:

1. search papers
2. create or update notes in `references/`
3. log meetings and action items in `meeting-note.md`
4. log hourly progress and backlog items during active work
5. develop ideas with theory notes and discussion
6. run simulations or empirical checks in `finding/`
7. integrate stable material into `deliverable/paper/`
8. create slides from `deliverable/paper/`

Short version:

`search -> note -> discuss -> think -> simulate -> paper -> slides`

## Prompt-Chained Workflow

When you want better performance by splitting work into separate prompts, use
this loop:

1. define the task queue in `TASKS.md`
2. ask Codex to execute exactly one task
3. let Codex update outputs plus `TASKS.md` and `SESSION.md`
4. start the next prompt from the recommended handoff in `SESSION.md`

Short version:

`queue -> execute one task -> record handoff -> next prompt`

This keeps each prompt narrow while still preserving continuity inside the repo.

## What Belongs In Each File

- `TASKS.md`: the ordered queue, status, scope, and definition of done
- `SESSION.md`: what just happened and what the next prompt should say
- `meeting-note.md`: higher-level research discussion, decisions, and coordination memory
- `BACKLOG.md`: good ideas that matter, but are not the next prompt

## Recommended Turn Shape

For best Codex performance, structure each prompt around a single unit of work:

1. point Codex to one task ID in `TASKS.md`
2. name the target files or deliverable
3. say whether Codex should stop after implementation or also document the result

Example prompt:

```text
Please work on T2 in TASKS.md.
Focus only on that task.
When finished, update TASKS.md and SESSION.md with the result and propose the next prompt.
```

## Automating Prompt Sending

If you do not want to manually type each prompt, use the repo-local runner:

```bash
make codex-task-prompt
make codex-task-next
make codex-task-resume
```

What each command does:

- `make codex-task-prompt`: prints the next generated prompt without sending it
- `make codex-task-next`: sends the next task as a fresh `codex exec` run
- `make codex-task-resume`: sends the next task to the most recent Codex session with `codex resume --last`

You can target a specific task:

```bash
make codex-task-next TASK=T2
```

You can also set a model:

```bash
make codex-task-next TASK=T2 MODEL=gpt-5
```

Task selection rule:

1. first task with status `in_progress`
2. otherwise first task with status `todo`

This means you can keep the queue in `TASKS.md` and repeatedly run one command
to move through the sequence.

## Source of Truth by Stage

- Early-stage understanding: Markdown notes and meeting notes
- Theory development: discussion, notes, and the current draft in `deliverable/paper/`
- Simulation and numerical checking: `finding/`
- Formal project narrative: `deliverable/paper/`
- Presentation narrative: `deliverable/slides/`

## Skill Map

- `paper-search`: search literature and prioritize high-value papers
- `paper-note`: turn papers into structured Markdown notes in `references/`
- `meeting-log`: maintain `meeting-note.md`
- `hourly-progress-log`: record compact hourly updates and backlog-worthy issues
- `theory-workbench`: reason through assumptions, proof ideas, and gaps
- `simulation-runner`: design and inspect simulations, using R by default
- `chat-to-latex`: integrate current discussion into `deliverable/paper/` only when explicitly requested
- `beamer-slides`: create or revise Beamer slides using the paper draft as the main source
- `chinese-referee-report`: draft or revise Traditional Chinese referee reports in `report/`
- `english-referee-report`: draft or revise English referee reports in `report/`
- `letter-to-editor`: write editor-facing confidential comments or letters in `report/`

## Important Conventions

- Use relative links for figures in Markdown notes.
- For paper-note figures, store files in `attachments/references/`.
- For meeting-note figures, store files in `attachments/meetings/`.
- Use R by default for simulation work unless the project clearly uses another language.
- Before integrating text into `deliverable/paper/`, check notation consistency with the paper draft.
- For slide work, match the style of existing Beamer decks when possible.
- For literature search, prioritize higher-quality journals when ranking candidate papers.

## Practical Guidance for Agents

- Start from local files before relying on memory.
- If `TASKS.md` and `SESSION.md` exist, use them first for multi-turn continuity.
- Inspect `deliverable/paper/` whenever project context is needed and the task touches the paper.
- Keep notes concise and structured so they remain useful later.
- Do not treat exploratory notes as finished manuscript text.
- Do not treat slides as the main place for developing ideas.
