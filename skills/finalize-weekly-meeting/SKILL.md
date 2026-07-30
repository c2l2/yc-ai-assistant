---
name: finalize-weekly-meeting
description: Finalize a manager-edited internal weekly report after the meeting, preserve a complete current task snapshot under Next Actions, and synchronize BACKLOG.md, DECISIONS.md, and RISKS.md from finalized weekly-report history. Use only when the manager explicitly confirms that the meeting is complete, identifies the target report, and requests both finalization and root synchronization.
---

# Finalize Weekly Meeting

Revise the completed internal report for the project manager and update the
three root current-state views. Only the manager can authorize this write
workflow.

## Authorization Gate

Proceed only when all of the following are true:

- the meeting has concluded;
- the manager identifies the target internal weekly report;
- the manager explicitly asks to finalize it and synchronize the root state.

If any condition is missing, do not edit the report or root documents.

## Inputs

Read:

1. the manager-edited target internal report in `report/`;
2. `yc-ai-assistant/templates/weekly-meeting.md`;
3. earlier finalized internal weekly reports when history is needed;
4. `TEAM.md` to validate members, owners, and reviewers;
5. existing `BACKLOG.md`, `DECISIONS.md`, and `RISKS.md` as current views.

The pre-meeting AI review may inform the discussion, but it is not a source of
project state. Only content retained in the manager-approved internal weekly
report may change the root documents.

## Workflow

Complete steps 1–9 as a read-only preflight. Do not write any file until the
preflight passes without material ambiguity.

1. Reconfirm that all authorization-gate conditions are satisfied.
2. Read the target report and preserve the manager's substantive meaning.
3. Draft the intended English revision in memory using exactly these sections:
   - `Meeting Goals / Agenda`
   - `Key Takeaways`
   - `Consensus and Decisions`
   - `Next Actions`
   - `Backlog & Unresolved Questions`
   - `Other`
4. Separate progress findings, decisions, actions, backlog items, risks, and
   unresolved questions without inventing content.
5. Add or normalize stable IDs only when the report unambiguously establishes a
   record:
   - tasks: `T-###`
   - backlog: `B-###`
   - decisions: `D-###`
   - risks: `R-###`
6. Compare the previous finalized report's active actions with the target
   report.
   Ensure every previously active action is completed, cancelled, reassigned,
   or carried forward explicitly. Do not silently drop or carry forward work.
7. Draft a complete `Next Actions` snapshot for the coming week in memory and
   validate all owners and reviewers against `TEAM.md`.
8. Draft the corresponding backlog, decision, and risk changes in memory.
9. If ambiguity could change an owner, deadline, task status, decision, backlog
   state, risk state, or the disposition of a previous action, stop and ask the
   manager without writing any file.
10. Write the revised report, preserve
    `document_type: internal-weekly-report` and
    `primary_audience: project-manager`, set `status: finalized`, and record the
    manager and finalization time.
11. Update root current-state views solely from finalized weekly-report
    history:
    - `BACKLOG.md`: current open backlog items;
    - `DECISIONS.md`: currently effective decisions;
    - `RISKS.md`: current open risks.
12. Link every root record to the latest weekly report that changed it.
13. Re-read every changed file and report the IDs created, changed, closed, or
    removed.

## Root-State Rules

- Assignment history and current assignments remain in internal weekly reports.
- Each finalized report's `Next Actions` is the complete task snapshot for the
  coming week, including explicit carryovers.
- Never create or update a root `TASKS.md`.
- Closed or promoted backlog items remain in reports, not the open root view.
- Superseded or revoked decisions remain in reports, not the effective root
  view.
- Resolved risks remain in reports, not the open root view.
- Never update `PROJECT.md`, `TEAM.md`, or `ROADMAP.md` through this skill.

## Guardrails

- Never synchronize from a draft report or from the pre-meeting AI review.
- Never infer a state change from Git activity alone.
- Do not add a task, owner, deadline, decision, backlog item, or risk absent
  from the finalized report.
- Improve language without changing meaning.
- Do not silently resolve conflicting or incomplete records.
- Never rewrite older finalized reports; record corrections in the current or
  a later weekly report.
- Do not run application tests or evaluate implementation in this skill.
- Apply the report revision and corresponding root updates in the same turn.
- Do not convert the internal report into a public-facing communication through
  this skill.

## Completion Report

Return:

```markdown
Finalized internal report: report/YYYY-MM-DD-weekly-meeting.md

Root synchronization:

- Backlog items added, updated, or closed:
- Decisions adopted, superseded, or revoked:
- Risks added, updated, or resolved:

Meeting actions:

- Tasks created, changed, completed, cancelled, or carried forward:

Unresolved items:

- None, or a concise list requiring manager input
```
