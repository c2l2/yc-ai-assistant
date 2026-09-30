---
name: submission-check
description: Review a research draft before submission, across all checks or selected scopes, using focused passes and saved checkpoints. Produce findings without editing the manuscript. Use other workflows for ordinary proofreading, referee reports, or revision.
---

# Submission Check

Review the draft as an author preparing to submit a paper. Find actionable
problems and explain their consequences, while making the depth and limits of
the review visible. Retain all supported findings; do not impose the short
comment limits used for referee reports.

## Select the scope

Keep this as one skill with selectable scopes. Interpret ordinary language such
as "proofs only" or "check the numbers" using the following names:

| Scope | Review focus |
| --- | --- |
| `theory` | Assumptions, definitions, formal results, and proofs |
| `evidence` | Empirical and simulation design, inference, and numerical support |
| `argument` | Contribution, positioning, interpretation, and strength of claims |
| `presentation` | Writing, notation, references, cross-references, and PDF layout |
| `submission` | The selected journal's requirements and submission materials |
| `all` | Every applicable scope, followed by cross-scope synthesis |

Default an unqualified submission check to `all`. Honor a requested scope,
combination of scopes, or specific result/section without expanding it to a full
audit. Read and apply only the relevant review-pass guidance below, plus the
shared workflow and reporting rules. Out-of-scope checks remain explicitly
unreviewed. If an incidental concern matters, record it as a follow-up without
silently starting another pass.

One request for `all` authorizes the full staged review; do not require the user
to send a new prompt or approve each pass. Separate prompts may select scopes
or resume unfinished work, but are not required for a thorough review.

## Inputs and boundaries

- Use the manuscript path supplied by the user. Otherwise identify the relevant
  main draft under `deliverable/paper/`, using local project context. Ask for
  clarification only if no draft can be found or multiple plausible drafts remain.
- Accept an optional target journal and article type. Recover these from explicit
  project context when available; do not infer a journal from a document class
  alone. A journal-independent review can proceed without this information.
- For `all`, read the complete supplied manuscript and relevant appendices
  across the passes. For selected scopes, read the relevant material fully and
  enough surrounding context to interpret it. Follow LaTeX `\input` and
  `\include` dependencies and consult directly relevant bibliography, figures,
  tables, code, outputs, and local references as needed.
- Treat the manuscript as the source of its claims and notation. Use Markdown
  research memory to clarify context, not to silently repair an unstated argument.
- This is a report-only workflow. Leave manuscript text, bibliography, figures,
  analysis code, and existing results unchanged. Put suggested replacements in
  the report. Subsequent manuscript revision requires a separate user request;
  follow the repo's LaTeX review conventions then.
- Default to focused verification. Do not launch full analysis or simulation
  pipelines, install dependencies, develop substantial new proofs, or prepare or
  submit journal materials as part of the check. Identify necessary follow-up
  work in the report.

## Staged execution and checkpoints

**Establish shared context before detailed checks.** Identify the draft and
available evidence, then map the research question, principal claims, notation,
assumptions, and dependencies needed for the selected scopes. An `all` review
needs a whole-paper overview; a narrow review needs only the relevant map.
Distinguish missing inputs from defects in the paper itself. Record content
hashes of the reviewed inputs, adding dependencies as they are discovered, and
the commit and working-tree status when available. All passes must refer to the
same draft version, including supplied PDFs and analysis outputs.

Choose the report destination using the output rules below. Before the first
detailed pass, create a companion `<report-stem>-work/` directory containing
`review-state.md`. Save the selected scopes, draft fingerprint, shared context
map, coverage table, links to pass notes, and next action there. This is the
handoff for subsequent prompts; do not depend on chat history alone.

**Run each selected scope as a focused pass.** For `all`, the default order is
`theory`, `evidence`, `argument`, `presentation`, then `submission`. Independent
passes may run in parallel; argument assessment must account for the technical
findings before it is finalized. An absent domain is `not applicable`; missing
materials or an unspecified journal leave affected checks `not checked` or
`partially checked` with a reason. Neither prevents the remaining passes.

Save each pass's evidence, findings, coverage, and unresolved dependencies to
`<scope>.md` in the work directory, then update `review-state.md` before moving
on. Checkpoints are substantive intermediate results, not headings added after
writing a final report. For long theory reviews, work through related theorem
and lemma dependencies in manageable batches, saving `theory-01.md`,
`theory-02.md`, and so on with a summary in `theory.md`. Carry the definitions
and assumptions each batch needs; do not split proofs at arbitrary page counts.

Maintain the coverage record by section, formal result, and selected review area.
Use `checked`, `partially checked`, `not checked`, and `not applicable`, with a
brief reason, including "outside requested scope" where appropriate. `Checked`
describes work performed, not a guarantee of correctness. Within a theory pass,
name every supplied theorem, lemma, proposition, corollary, and proof in scope.
Do not mark an overview or sampled proof as a completed detailed check.

**Resume from evidence.** Read the active state and pass notes and compare input
hashes before reusing earlier coverage. Recheck hashes before synthesis too.
If inputs changed, retain the earlier notes but mark affected checks stale and
recheck the changed material and its dependent claims; do not combine versions
into a single completed review. Continue unaffected work without restarting
everything. If a limit prevents completion, save partial findings, exact
remaining coverage, and the best next action. Report the limitation and link
the checkpoint rather than compressing the remaining passes into a superficial
claim of completion. Continue autonomously while the task remains feasible.

**Synthesize after the selected passes.** Resolve duplicate or conflicting
findings against the source. For `all`, revisit the abstract, introduction, and
conclusion in light of the technical findings, checking that claims, notation,
results, and interpretation agree across sections. Prioritize remedies and
identify unresolved dependencies. For a scoped review, synthesize only the
requested checks and state that this is not an overall submission-readiness
assessment. Keep pass notes accessible from the final report.

For PDF-only inputs, review the available text and rendered pages needed for
the selected scopes, locating findings by PDF page and visible labels. Mark
source-level checks unavailable.
If extraction or rendering is unavailable, state which content could not be
inspected and continue the checks supported by the available evidence. A missing
appendix or inaccessible source is not evidence that its argument is wrong.

## Review passes

### `argument`: argument and contribution

- Reconstruct the research question, contribution, setting, and principal claims.
  Compare the title, abstract, introduction, results, and conclusion for changes
  in scope, strength, or interpretation.
- Check that claimed novelty and comparisons with prior work have support.
  Distinguish a demonstrated misstatement from an unverified novelty claim; a
  submission check does not establish an exhaustive literature search.
- Identify missing motivation, unexplained transitions, unsupported generality,
  causal overstatements, and conclusions that exceed the evidence. Explain the
  specific reader misunderstanding or substantive consequence.

### `theory`: theory and mathematical consistency

- Review every supplied formal statement and proof in scope, including relevant
  appendices. Map each conclusion to its assumptions and the results it depends
  on; explicitly label dependencies whose proofs were not checked.
- Check definitions, quantifiers, domains, dimensions, symbol reuse, and agreement
  between theorem statements and the results actually established by the proofs.
- Inspect logical steps, hidden regularity or identification assumptions, uses of
  external theorems, limit operations, boundary cases, and circular dependencies
  where relevant. Use small counterexamples or calculations to test suspect
  claims when feasible.
- Distinguish an incorrect result, an incomplete proof, an unstated assumption,
  and an exposition issue. Explain the exact gap rather than substituting a
  plausible argument and declaring the original proof sound.
- When a cited result is essential, inspect the supplied source or consult its
  primary source. If it cannot be verified, record the dependency as unverified.

### `evidence`: empirical and simulation evidence

- Where applicable, check the connection between the question, estimand, design,
  identification assumptions, estimator, and reported interpretation.
- Inspect sample definitions, units, transformations, uncertainty measures,
  comparison methods, and robustness claims against available methods, code,
  and outputs. For simulations, inspect the stated data-generating process,
  parameter settings, replications, and Monte Carlo uncertainty where relevant.
- Reconcile numbers, signs, magnitudes, sample sizes, and significance claims
  across prose, equations, tables, and figures. Check captions and notes for the
  information needed to interpret results.
- Assess what the provided artifacts permit someone to reproduce. Do not call
  results reproduced merely because code exists or reported numbers agree.
  Missing data or code limits verification; it does not by itself disprove results.

### `presentation`: writing, references, and presentation

- Check clarity, grammar, terminology, abbreviations, and consistent notation.
  Keep optional stylistic improvements distinct from errors that change meaning.
- Check equation explanations, labels, cross-references, appendix pointers,
  citations and bibliography entries, figure axes, units, legends, and captions.
  Distinguish a missing bibliography entry from an entry whose accuracy has not
  been independently verified. Do not invent replacement references.
- Inspect the rendered PDF when available for clipped or illegible content,
  unresolved references, poor equation breaks, and misplaced tables or figures.
  Link visual findings to page numbers and source locations when possible.

### `submission`: journal requirements

When a target journal is known, consult its current official author instructions
for the relevant article type. Link the sources and record the access date.
Check applicable length and format rules, anonymization, title-page treatment,
abstract and keywords, disclosures, data or code statements, supplements, and
required submission materials. Distinguish confirmed requirements from advice
and requirements that depend on an unknown article type. Flag missing materials
without drafting them or making declarations on the author's behalf.

If official guidance cannot be accessed, mark the affected requirements
unverified. If no target journal is supplied, mark journal compliance
`not checked — target journal unspecified`; continue any other selected passes
without assigning a journal or inventing submission rules.

## Focused verification

- During `presentation`, or when another selected check needs rendered evidence,
  inspect available build instructions and tooling. When feasible, compile a
  scratch copy with the existing engine and bibliography workflow; direct all
  generated files there. Avoid build commands that edit or overwrite original
  sources or published artifacts. A scoped theory check does not require an
  unrelated build or layout audit.
- Read build diagnostics and inspect the resulting PDF. A successful build does
  not establish correct references, good layout, or mathematical validity. If
  compilation or PDF inspection fails, record the cause and use existing
  artifacts or source inspection for the remaining checks.
- Use short, isolated calculations to resolve specific arithmetic or mathematical
  questions. Inspect scripts before running them; use existing analysis outputs
  without starting a full replication job. Report what was run and what it
  actually establishes.
- Missing tools should limit only the checks that need them. Do not install new
  tools or silently downgrade an unperformed check to a passing result.
- Delegate independent passes or proof batches when useful and available. Give
  reviewers the same draft version, relevant context map, and explicit scope.
  Each reviewer writes its own pass notes; the coordinator owns the shared state,
  consolidates findings, and assigns final issue IDs to avoid conflicting edits.
  Delegation is optional; saved passes also apply to a single-agent review.

## Report output

Save the complete report in the established paper-specific folder under
`report/`, or create `report/<paper-slug>/` using a short ASCII, hyphen-separated
identifier derived from the manuscript title or entrypoint filename.

Use `YYYY-MM-DD-submission-check.md` with the current local date, and label the
selected scopes prominently inside it. Never overwrite an earlier report: for
a new review, if either that filename or its companion work directory exists,
use the first available suffix `-2`, `-3`, and so on before `.md` and `-work/`.
Honor an explicit user-supplied destination.

When continuing an existing review, update its active state and pass notes;
preserve any report already issued and choose a new filename for an updated
synthesis. Link that report to the existing work directory. If no report was
issued yet, use the reserved filename. Share the issue IDs and coverage across
continuations, and retain earlier-version evidence when checks become stale.

Write the report in the language of the invoking request unless the user specifies
another language. Keep quoted passages and proposed replacement text in the
manuscript's language. Suggested LaTeX belongs in the report, not in the draft.

Use the following structure, expanding it to retain every supported finding:

1. **Review basis and coverage:** requested scopes, target manuscript/version,
   journal if known, reviewed files and artifacts, completed and unreviewed
   checks, section and relevant formal-result coverage, unavailable material or
   tools, and links to the checkpoint and each pass's findings.
2. **Assessment:** for `all`, leading issues to resolve before submission and
   what the completed checks support; for selected scopes, conclusions limited
   to those scopes, without an overall readiness verdict. If no material issues
   were found, say "No material issues found in the completed checks" with remaining limitations;
   do not certify correctness or predict acceptance.
3. **Findings by priority:** submission blockers, major issues, and minor issues.
   Blockers prevent a valid submission or undermine a central result; major
   issues materially affect support, interpretation, or comprehensibility; minor
   issues are localized correctness or presentation problems. Use priority for
   impact, and separately label evidence as confirmed or tentative. Missing
   evidence belongs in coverage unless it supports a concrete manuscript issue.
4. **Optional improvements:** clearly separate preferences and useful extensions
   from necessary corrections.
5. **Revision checklist:** order actions by dependency and importance, reference
   finding IDs, and identify any follow-up verification or full replication.

Assign findings stable IDs such as `SC-001`. For each finding include:

- priority and evidence status;
- exact location: for findings tied to available LaTeX source, the actual `.tex`
  file path and one-based line number, plus section, equation, theorem, table,
  or figure label when available; for example,
  `deliverable/paper/sections/results.tex:42` (Table 2);
- evidence: a short passage, calculation, failed proof step, or conflicting
  entries that the author can check;
- consequence: why this matters for the paper or submission;
- suggested remedy, preserving the manuscript's intended meaning and notation;
- resolution criterion: what change or verification would resolve the issue.

Include these source locations in both pass notes and the final report. Point
to the included `.tex` file that contains the relevant text, not just its
`\input` or `\include` command in the main file. For inconsistencies across
passages, cite each relevant location. Verify line numbers with numbered source
reads such as `nl -ba` or `rg -n` against the reviewed on-disk version, and refresh
them for the current report after source changes. Section labels and PDF pages
supplement available `.tex` line references; they do not replace them. When no
source location applies or the source is unavailable, state that limitation and
use the best available anchor, such as a PDF page or journal-rule link. Never
invent `.tex` line numbers from extracted PDF text.

Consolidate repeated instances of the same issue while listing their locations.
When reviewing a revised draft with an earlier report, preserve existing issue
IDs, mark their current status, and assign new IDs only to new findings. Check
each proposed issue against its surrounding text before retaining it.

Return a concise chat summary of the principal findings and coverage limits,
with a link to the complete report. Do not repeat an unbounded report in chat.

## Example requests

- "Use submission-check for theory only, including the appendix proofs."
- "Check evidence and argument; leave writing and journal requirements for later."
- "Check all scopes in separate passes and save one consolidated report."
- "Resume the submission check from its saved review-state.md."
