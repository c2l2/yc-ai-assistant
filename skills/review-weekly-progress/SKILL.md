---
name: review-weekly-progress
description: Perform a read-only pre-meeting review of a team-written internal weekly report for the project manager. Use when the manager asks to compare members' claimed progress with new Git commits and local deliverables, assess each member's contribution, identify blockers, recommend the most important next step, or prepare discussion points. Do not edit files or run builds, tests, simulations, notebooks, servers, or application code.
---

# Review Weekly Progress

Produce an evidence-based internal manager briefing in chat. Inspect new
committed work without executing it, and keep every recommendation nonbinding
until the team discusses it.

## Read-Only Boundary

- Do not create, edit, rename, or delete any file.
- Do not update the internal weekly report or any root project document.
- Do not run builds, tests, simulations, notebooks, servers, application code,
  or generated code.
- Use only read-only file inspection and Git history or diff commands.
- Return the review in chat. Never save a separate review file through this
  skill.

## Inputs

Read only the files needed for the review:

1. the upcoming member-written internal report at
   `report/YYYY-MM-DD-weekly-meeting.md`;
2. the previous finalized internal weekly report;
3. earlier finalized reports only when needed to trace a cited task ID;
4. `PROJECT.md`, `ROADMAP.md`, and `TEAM.md`;
5. new commits since the previous meeting and the files changed by them;
6. evidence linked in the upcoming report;
7. `BACKLOG.md`, `DECISIONS.md`, and `RISKS.md` only when they affect priority,
   dependencies, or blockers.

Use Git author identities in `TEAM.md` to map commits to members. Report missing
or ambiguous mappings instead of guessing.

## Workflow

1. Identify the review window:
   - use the previous finalized report's `finalized_at` as an exclusive lower
     time bound and the current `HEAD` as the inclusive upper bound;
   - if this is the first review, or `finalized_at` is missing, require a
     manager-provided base commit or date;
   - if no valid base is available, report the evidence gap and do not treat
     older commits as new progress.
2. Extract each member's claimed progress, task IDs, evidence, blockers, and
   proposed next step from the upcoming report.
3. Inspect the relevant commits, diffs, changed files, and committed
   deliverables for that window.
4. Compare each claim with the most recent assignment and definition of done
   recorded under `Next Actions` in finalized weekly-note history. Follow older
   notes only as far as needed to resolve a cited task ID.
5. Identify committed work that the member did not mention.
6. State any completion condition that cannot be checked without execution,
   external access, or human judgment.
7. Assess blockers, dependencies, workload conflicts, and missing evidence.
8. Recommend exactly one most important next step and explain what it unblocks.
9. Propose a small work breakdown and possible owners for meeting discussion.
10. Return one manager report in chat and make no file changes.

State the exact base date or commit and upper-bound commit in the report.

## Evidence Labels

Use claim-level labels:

- `Supported by repository evidence`
- `Partially supported`
- `Not evidenced in the review window`
- `Requires runtime or human verification`
- `Not assessable from available evidence`

Use task-level status:

- `on track`
- `at risk`
- `blocked`
- `insufficient evidence`

A commit proves that a repository change was recorded. It does not by itself
prove quality, completion, acceptance, effort, or sole authorship.

## Manager Report Format

```markdown
# Internal Manager Weekly Progress Review

## Review Scope and Evidence Limits

## Executive Summary

## Member-by-Member Review

### [Member]

- Assigned outcome:
- Claimed progress:
- Observed commits and changed files:
- Repository evidence:
- Assessment:
- Remaining definition-of-done items:
- Blockers and dependencies:
- Work not mentioned in the report:
- Questions to discuss:

## Cross-Team Dependencies and Risks

## Most Important Next Step

- Recommendation:
- Why now:
- What it unblocks:
- Confidence:
- Lower-ranked alternatives:

## Proposed Work Breakdown for Discussion

- Proposed task, owner, reviewer, and definition of done
- Label every assignment as a discussion proposal

## Items Requiring Manager Verification
```

## Guardrails

- Do not rank people or calculate personal performance scores.
- Do not equate commit count, lines changed, or message volume with progress.
- Distinguish missing evidence from missing work.
- Do not attribute shared or co-authored work to one member without evidence.
- Do not infer completion from a member's statement alone.
- Treat runtime-dependent claims as unverified rather than failed.
- Keep recommended priorities and assignments nonbinding.
- Treat the weekly report and review as internal management material; do not
  convert them into public-facing communications through this skill.
