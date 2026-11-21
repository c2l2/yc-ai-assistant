---
name: theory-workbench
description: Develop theoretical ideas, sketch proofs, check assumptions and diagnose gaps. Use also for an independent second reading of a proof intended for the paper.
---

# Theory Workbench

Use this skill when the user is doing theory-heavy research and wants Codex to help reason through a claim rather than just summarize or rewrite notes.

The goal is to make theoretical thinking explicit, structured, and reusable. A good output should separate formal claims from intuition, identify which assumptions matter, and make uncertainty visible instead of hiding it.

## What to inspect

Inspect only the files needed for the task:

- relevant Markdown notes in `references/`
- the latest finalized `report/YYYY-MM-DD-weekly-meeting.md` if recent
  discussions matter for the theory idea
- any theory sketch, derivation, proof outline, or pasted math provided by the user
- relevant LaTeX files in `deliverable/paper/` if the theory idea is already being drafted there

Treat the most relevant LaTeX file in `deliverable/paper/` as a high-value context source because it often contains the latest project progress and the most mature statement of the argument.

## Output targets

Default output is one of the following, depending on the user's request:

- a structured proof sketch
- a list of assumptions and implications
- a diagnosis of gaps or weak points in an argument
- LaTeX text that can be pasted directly into a draft when the user explicitly asks for it or when the argument is sufficiently stable
- a compact Markdown note only when the user explicitly wants a note-oriented result


## Writing rules

- Separate formal claims from intuition.
- State explicitly when something is a conjecture rather than a proved result.
- Identify which assumption is doing the most work.
- Prefer transparent reasoning over polished but vague prose.
- Flag gaps honestly instead of smoothing them over.
- When helpful, suggest counterexamples, edge cases, or failure modes.
- Keep links to related local notes short and useful.
- Default to structured reasoning and proof-sketch output during exploration.
- Produce LaTeX only when the user explicitly asks for it or when the argument is sufficiently stable for drafting.

## Reasoning standards
- Do not present an incomplete proof as complete.
- If the argument depends on a hidden step, name it explicitly.
- If multiple proof strategies are plausible, compare them briefly.
- Distinguish between mathematical necessity and modeling convenience.
- When a result seems false or fragile, say so clearly and explain why.

For proof-oriented work, prefer this sequence:

1. clarify the claim
2. list the assumptions
3. sketch the proof logic
4. identify missing steps or fragile points
5. iterate until the argument is stable
6. convert to LaTeX only at the end if requested

## A second reader for a consequential proof

Use this option when the author asks for an independent check or an important result is about to enter the manuscript and depends on a fragile step. Keep early exploration conversational.

Give a fresh reader the exact proposition, assumptions, definitions, current proof and any lemmas it invokes. Start a separate agent or session without the drafting conversation. Exclude earlier verdicts, the author's expected answer and other reviewers' notes from the materials available to it. If the available tool shares that history, describe your own second pass as a self-check.

Ask the reader to rederive the critical implication. For an objection, request the first unsupported line, the assumption or inequality it needs, and a derivation or counterexample when available. For a sound step, ask which condition makes it work. Reconcile its reasoning against the actual proof before reporting a correction. Distinguish a gap in this proof from a false proposition. Apply any resulting manuscript edit under the project's existing agreement with the author.

When testing a **change to this review skill**, use a correct proof and a disposable copy with one known defect. Give each to a separate fresh reader under the same neutral instructions, without access to the other copy or the answer key. Check both whether the defect was located and whether the sound proof drew a false objection. This exercise belongs to skill development. The user's live manuscript is never the test fixture. [Reviewer calibration](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/vaccinate/SKILL.md)

## Good output standard

A good output should let a future reader quickly answer:

- What is being claimed?
- What assumptions are needed?
- Why might the argument work?
- Where might it fail?
- What should be tried next?

Default to medium detail: detailed enough to support serious theory work, short enough to remain usable as a working note.

## Example prompt patterns

Use this skill when the user asks things like:

- help me think through this proof sketch
- what assumptions do I need for this claim
- identify the weak point in this argument
- turn these theory notes into a cleaner structure
- connect this idea to my other notes
- help me convert this theory sketch into a LaTeX-ready outline
