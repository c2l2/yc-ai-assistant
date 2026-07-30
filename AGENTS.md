# AGENTS.md

## Repo Purpose

This repository is a reusable workspace for:

- theoretical research in econometrics, statistics, and related fields;
- empirical research in economics, data science, and related fields;
- software and application development involving data science, statistics, or
  research workflows.

The repository is designed so that:

- Markdown stores working research and project memory;
- LaTeX in `deliverable/paper/` stores an evolving formal draft when the
  project includes a paper;
- files in `deliverable/slides/` are presentation artifacts, often initialized
  from the paper draft and later revised in place;
- software or application deliverables can live in `deliverable/app/`;
- Codex can use local files to support the relevant parts of the workflow.

Do not assume that every project uses every folder or workflow in this
template. Prefer project-specific local context over template defaults.

All paths below are relative to the project root. When `yc-ai-assistant` is
used as a submodule, the project root is its parent.

## Global Interpretation Rules

- Treat Markdown as the canonical working memory for research ideas, project
  context, coordination, and decisions.
- When a task concerns a paper, theory, notation, or initializing slides, treat
  the most relevant LaTeX file in `deliverable/paper/` as the formal source of
  current context.
- For slide revision tasks, treat the target Beamer file and its inline comments
  as the main working source. Consult `deliverable/paper/` only when needed for
  notation, factual consistency, or current framing.
- Treat `deliverable/slides/` as a presentation layer derived from the paper,
  findings, or approved project material, not as the main place to develop
  ideas.
- For empirical or software tasks, prioritize the relevant project context,
  source code, data documentation, and current outputs.
- Apply weekly team-management rules only when the project actually uses that
  workflow.
- Prefer local repository evidence over unsupported assumptions.

## Folder and File Meaning

- `PROJECT.md`: optional project purpose, scope, constraints, outcomes, and
  current focus.
- `TEAM.md`: optional team roster, roles, responsibilities, Git identities,
  capacity, and review areas.
- `ROADMAP.md`: optional priorities, milestones, definitions of done, and
  dependencies.
- `BACKLOG.md`: optional current open backlog derived from finalized internal
  weekly reports when the weekly workflow is used.
- `DECISIONS.md`: optional currently effective decisions derived from finalized
  internal weekly reports.
- `RISKS.md`: optional current open risks derived from finalized internal
  weekly reports.
- `references/`: paper PDFs, source material, and Markdown reading notes.
- `attachments/meetings/`: images used by internal weekly meeting reports.
- `attachments/references/`: images used by paper and reading notes.
- `data/raw/`: source data that should remain unchanged when practical.
- `data/processed/`: cleaned or transformed data.
- `data/temp/`: disposable intermediate data.
- `data/code/`: data-processing and analysis code when the project uses this
  layout.
- `finding/`: empirical results, simulations, figures, and intermediate
  research outputs.
- `report/`: Markdown reports and, when enabled, internal weekly management
  reports named `YYYY-MM-DD-weekly-meeting.md`.
- `deliverable/paper/`: manuscript and formal paper files.
- `deliverable/slides/`: Beamer slides and other presentation artifacts.
- `deliverable/app/`: software or application deliverables.
- `templates/`: reusable project, data, finding, and report templates.
- `yc-ai-assistant/templates/`: templates used by repo-local AI workflows,
  including the weekly meeting template.
- `yc-ai-assistant/skills/`: task-specific Codex skills.
- `yc-ai-assistant/TASKS.md`: manual internal record for maintaining the shared
  AI template; it is not a project or team task register.

## Context Priority

Build only the context needed for the task.

### Paper and theory

1. the most relevant file in `deliverable/paper/`;
2. directly relevant files in `references/`;
3. relevant project context or finalized weekly reports;
4. directly relevant files in `finding/`;
5. templates only when creating a new artifact.

### Slides

1. the target file in `deliverable/slides/` and its inline comments when
   revising an existing deck;
2. the most relevant file in `deliverable/paper/` when initializing slides or
   checking notation, facts, or framing;
3. directly relevant findings, approved project material, and style references;
4. templates only when creating a new artifact.

### Empirical, data, and software work

1. `PROJECT.md`, `ROADMAP.md`, and the directly relevant source or deliverable;
2. relevant data documentation and code;
3. directly relevant findings and outputs;
4. the latest finalized weekly report when coordination context matters;
5. references and templates only when needed.

### Weekly progress review

1. the upcoming team-written internal weekly report;
2. the previous finalized weekly report and its `Next Actions`;
3. `PROJECT.md`, `ROADMAP.md`, and `TEAM.md`;
4. new commits and relevant committed diffs since the previous meeting;
5. evidence linked from the report;
6. `BACKLOG.md`, `DECISIONS.md`, and `RISKS.md` when relevant.

Do not read broadly without need.

## Workflow Conventions

- Use structured Markdown so research and project memory remains reusable.
- Use relative links for Markdown images.
- Keep paper-note images in `attachments/references/`.
- Keep weekly-meeting images in `attachments/meetings/`.
- Use R by default for simulations unless the project clearly uses another
  language or stack.
- Match notation to the existing LaTeX draft before adding manuscript text.
- Integrate the current chat into `deliverable/paper/` only when the user
  explicitly asks.
- Before integrating text into the paper, show the proposed LaTeX in chat.
- For literature search, prioritize stronger journals, especially in
  economics, econometrics, statistics, data science, and the user's preferred
  management-science subfields.
- For slides, match the project's established Beamer or presentation style
  when possible.
- For slide revision tasks, treat inline LaTeX comments in
  `deliverable/slides/` as authoritative local instructions.
- For software work, follow the existing stack and repository conventions and
  verify changes in proportion to their risk.

## Optional Weekly Team Workflow

Use this workflow only for projects with weekly team coordination.

### Sources of truth

- Finalized internal weekly reports in `report/` are the history of task
  assignments, decisions, backlog, risks, and unresolved questions.
- The latest finalized internal report's `Next Actions` is the current task and
  assignment snapshot. Unfinished work must be carried forward explicitly.
- `BACKLOG.md`, `DECISIONS.md`, and `RISKS.md` are optional current-state views
  derived only from finalized internal weekly reports.
- `PROJECT.md`, `TEAM.md`, and `ROADMAP.md` are manager-maintained context.
- Git commits are evidence that changes were recorded, not proof of quality,
  completion, effort, acceptance, or sole authorship.

### Internal weekly reports

- Treat each weekly meeting file as an internal management report whose primary
  audience is the project manager.
- Store reports directly under `report/` as
  `YYYY-MM-DD-weekly-meeting.md`.
- Start from `yc-ai-assistant/templates/weekly-meeting.md`.
- Team members write their own progress before the meeting.
- Keep the finalized internal report in English.
- Preserve these six sections:
  - `Meeting Goals / Agenda`
  - `Key Takeaways`
  - `Consensus and Decisions`
  - `Next Actions`
  - `Backlog & Unresolved Questions`
  - `Other`
- Every previous action must be completed, cancelled, reassigned, or carried
  forward explicitly before finalization.

### AI review and finalization

- `review-weekly-progress` is read-only. It inspects the upcoming report,
  relevant finalized history, and new committed work, then returns an internal
  manager briefing in chat.
- The review skill must not edit files or run builds, tests, notebooks,
  simulations, servers, or application code.
- `finalize-weekly-meeting` may run only after the manager identifies the
  report, confirms that the meeting is complete, and explicitly requests
  finalization and synchronization.
- The finalizer may revise the identified report and update `BACKLOG.md`,
  `DECISIONS.md`, and `RISKS.md` solely from the finalized internal report.
- Team members may edit implementation artifacts and the upcoming draft report.
  For management records, they edit only that report.

### Assessment rules

- Evaluate claims against assigned outcomes, definitions of done, committed
  changes, and available evidence.
- Analyze each member's contribution without ranking people.
- Do not use commit counts, lines changed, hours, or message volume as
  productivity scores.
- Distinguish missing evidence from missing work.
- Mark runtime-dependent claims as requiring verification; do not run them
  during the weekly review.
- Recommend one most important next step and label proposed assignments as
  discussion proposals.

## Skill Usage

Use repo-local skills when the task matches:

- `paper-note`
- `theory-workbench`
- `paper-search`
- `simulation-runner`
- `beamer-slides`
- `revise-beamer-slides`
- `chat-to-latex`
- `chinese-referee-report`
- `english-referee-report`
- `letter-to-editor`
- `review-weekly-progress`
- `finalize-weekly-meeting`

Skills provide task-specific rules. This file provides global template-level
rules.

## Output Philosophy

- Help with structuring, critique, synthesis, writing, implementation, and
  continuity.
- Do not over-polish exploratory ideas into false certainty.
- Separate facts, interpretations, recommendations, and approved decisions.
- Be explicit about uncertainty, assumptions, evidence limits, and gaps.
- Prefer concise, reusable outputs over long generic prose.

## Sequential Prompt Protocol

When the user explicitly wants work split across separate prompts:

1. identify the canonical project file that should carry status and context;
2. work on one scoped task at a time unless the user asks to batch;
3. update the relevant status or handoff in that canonical file when
   authorized;
4. use the latest finalized internal report's `Next Actions` for coordinated
   team work;
5. prefer local files over long chat-only context.

Use `yc-ai-assistant/TASKS.md` only when maintaining the shared AI template.
It is a manual internal record and must not be treated as the project's task
queue. No automatic task runner is assumed.
