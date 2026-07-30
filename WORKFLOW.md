# Weekly Team Workflow

This workflow treats each weekly meeting file as an internal report to the
project manager. Team reporting remains human-authored and management decisions
remain human-controlled. AI reads and evaluates before the meeting, then
documents and synchronizes only after the manager approves the outcome.

All paths are relative to the parent project root.

## Core Loop

```text
committed work
      +
member-authored internal weekly report
              ↓
read-only AI manager review
              ↓
manager and team discussion
              ↓
manager edits the internal report
              ↓
manager-invoked finalization
              ↓
finalized actions + non-task root state
```

## 1. Team Work and Reporting

During the week, members:

1. complete their assigned work;
2. commit the work to the repository;
3. write their own update in the upcoming internal report at
   `report/YYYY-MM-DD-weekly-meeting.md`.

Each update should identify:

- assigned task or intended outcome;
- completed work;
- relevant commits, changed files, or other evidence;
- definition-of-done status;
- blockers and dependencies;
- proposed next step.

AI does not draft these member updates. The report's primary audience is the
project manager.

## 2. Read-Only Manager Review

Before the meeting, the manager invokes `review-weekly-progress`.

The skill reads:

- the upcoming internal report;
- the previous finalized report, including current assignments in
  `Next Actions`;
- the roadmap;
- team roles and Git author identities;
- new Git commits and relevant committed diffs;
- linked evidence.

The skill does not:

- edit the report or root documents;
- run tests, builds, simulations, notebooks, servers, or application code;
- infer quality or completion from commit volume;
- produce a permanent review file.

The review window starts after the previous finalized report's `finalized_at`
time and ends at the current `HEAD`. For the first review, or when that time is
missing, the manager must provide a base date or commit; the skill does not
treat older history as new progress.

It returns an internal manager briefing in chat containing:

- an executive summary;
- a member-by-member claim and evidence assessment;
- remaining definition-of-done items;
- blockers, dependencies, and unreported committed work;
- one recommended next step;
- proposed assignments for meeting discussion;
- items requiring manager or runtime verification.

## 3. Meeting Discussion

The manager uses the AI review as a discussion aid, not as an automatic
evaluation record.

During or after the meeting, the manager edits the internal weekly report to
record:

- accepted progress and important findings;
- actual consensus and decisions;
- agreed next actions and assignments;
- backlog changes;
- risks and mitigations;
- unresolved questions.

Only content retained in this manager-edited note may update root state.

## 4. Finalization and Root Synchronization

After the meeting, the manager explicitly invokes `finalize-weekly-meeting` and
identifies the internal report.

The skill:

1. revises the report into clear English without changing meaning;
2. preserves the six canonical sections;
3. adds or normalizes stable task, backlog, decision, and risk IDs when
   unambiguous;
4. asks the manager about material ambiguity rather than guessing;
5. marks the report `finalized`;
6. ensures `Next Actions` contains every active assignment for the coming week,
   including explicit carryovers;
7. updates:
   - `BACKLOG.md`
   - `DECISIONS.md`
   - `RISKS.md`
8. links every current root record to the weekly report that last changed it.

The finalizer never uses the pre-meeting AI report or Git activity alone to
create state.

## Current-State Meaning

- latest finalized report, `Next Actions`: current tasks and assignments
- `BACKLOG.md`: current open backlog
- `DECISIONS.md`: currently effective decisions
- `RISKS.md`: current open risks

All assignment history and task state remain in internal weekly reports. Closed
backlog, superseded decisions, and resolved risks also remain there.

## Stable IDs

- Tasks: `T-###`
- Backlog: `B-###`
- Decisions: `D-###`
- Risks: `R-###`
- Team members: `TM-###`

IDs support cross-week continuity. They do not replace readable descriptions.

## Weekly Internal Report Structure

Use `yc-ai-assistant/templates/weekly-meeting.md` and preserve:

1. `Meeting Goals / Agenda`
2. `Key Takeaways`
3. `Consensus and Decisions`
4. `Next Actions`
5. `Backlog & Unresolved Questions`
6. `Other`

Store reports directly in `report/` with the name
`YYYY-MM-DD-weekly-meeting.md`.

Before finalization, every action from the previous meeting must be completed,
cancelled, reassigned, or carried forward explicitly. This makes the latest
finalized report sufficient for the next review.

## No Automation Layer

This workflow intentionally has:

- no progress-running or progress-testing script;
- no automated state replay;
- no preview/apply command;
- no workflow regression test suite;
- no background update process.

Human review and explicit manager invocation are the control points.
