# Task Queue

Use this file when the work is intentionally split across multiple prompts.

## How To Use

- Keep tasks small enough that Codex can finish one in a single turn.
- Put tasks in the order you want Codex to attempt them.
- Mark exactly one task as `in_progress` at a time.
- Move important but deferrable ideas to `BACKLOG.md`.
- At the end of each turn, update statuses and note the next recommended prompt in `SESSION.md`.

## Status Legend

- `todo`
- `in_progress`
- `blocked`
- `done`

## Active Sequence

Workshop deck: "Empirical Bayes" (09:00 session). Two agenda blocks, each split
into one slide-drafting task per outline sub-point so each can be executed and
reviewed independently. No slides should be produced until the user approves
individual task cards — this table is the planning/queue stage only.

| ID | Status | Task | Output / Deliverable | Notes |
| --- | --- | --- | --- | --- |
| W0 | done | Set up the Beamer deck skeleton (preamble, title slide, section dividers for Part 1 / Part 2) matching `beamer-slides` skill style guide. | `deliverable/slides/eb-workshop.tex` | No content slides yet — just the shell all later tasks slot into. |
| W1 | done | Part 1 #1 — What is EB? When is it used? | Slide draft (outline first, then Beamer) | See task card W1 below. ~2 slides. Drafted directly into `eb-workshop.tex`. |
| W2 | done | Part 1 #2 — Teacher value-added: EB for individual estimates. | Slide draft | See task card W2. Drafted as 3 slides (split beyond the ~2 estimate). |
| W3 | done | Part 1 #3 — Teacher value-added: distribution of teacher effects. | Slide draft | See task card W3. Drafted as 3 slides (split beyond the ~2 estimate). |
| W4 | done | Part 1 #4 — Teacher value-added: using the teacher effect as a regressor (attenuation bias + EB fix). | Slide draft | See task card W4. Drafted as 3 slides (matches the ~2–3 estimate). |
| W5 | done | Part 1 #5 — Other unit types: judge effects, firm effects, and the general "many units" list. | Slide draft | See task card W5. Drafted as 2 slides (matches the ~2 estimate). |
| W6 | done | Part 1 #6 — Ranking application: Kline–Rose–Walters discrimination study. | Slide draft | See task card W6. Drafted as 3 slides (matches the ~3 estimate). |
| W7 | done | Part 1 #7 — A/B testing application: Azevedo et al. fat tails. | Slide draft | See task card W7. Drafted as 3 slides (matches the ~3 estimate). |
| W8 | done | Part 1 #8 — Wrap-up: when is EB used (synthesis slide). | Slide draft | See task card W8. Drafted as 2 slides (matches the ~1–2 estimate). |
| W9 | done | Part 1 #9 — Bridge: introduce the simplest EB (normal/normal), example-driven, light touch. | Slide draft | See task card W9. Drafted as 4 slides (matches the ~3–4 estimate). |
| W10 | todo | Part 2 #1 — Normal/normal setup: sampling distribution, prior, posterior mean derivation. | Slide draft | See task card W10. ~4–5 slides. Depends on W9. |
| W11 | todo | Part 2 #2 — From Bayes to Empirical Bayes: estimating hyperparameters from data. | Slide draft | See task card W11. ~3–4 slides. Depends on W10. |
| W12 | todo | Part 2 #3 — James–Stein phenomenon and the shrinkage-reduces-risk intuition. | Slide draft | See task card W12. ~4–5 slides. Depends on W11. |

Rough slide-count total: ~9 slides (skeleton + wrap-up) + ~20 slides (Part 1,
09:00–09:40) + ~12–14 slides (Part 2, 09:40–10:40) ≈ **low-to-mid 40s**. Treat
all counts as first-pass estimates to be revised once drafting starts — dense
image-heavy slides may need to split further.

## Toy Demo History

Tasks T1–T3 (`toy-demo.md` purpose/checklist/completion-note additions) were
completed earlier to validate the `make codex-task-*` automation. They are no
longer part of the active queue; see git history for that content if needed.

## Task Template

Copy this block when you need more detail for a task:

```md
### T#

- Status: `todo`
- Goal:
- Inputs:
- Target files:
- Definition of done:
- Depends on:
- Notes for Codex:
```

## Workshop Task Cards

Detailed cards for the "Empirical Bayes" workshop deck (see Active Sequence
table above for status/order). Each card is scoped to be draftable in one
turn: produce a slide-content outline first (bullets + figure placeholders),
not final Beamer LaTeX, unless the user asks to go straight to `.tex`.

### W0

- Status: `done`
- Goal: Create the Beamer shell for the whole workshop deck — preamble, title
  slide, and section-divider frames for "Part 1: Overview" and "Part 2:
  Point Estimation." No content slides.
- Inputs: `yc-ai-assistant/skills/beamer-slides/SKILL.md` style guide (default
  preamble block); no existing deck to match since `deliverable/slides/` was
  empty (only `.gitkeep`).
- Target files: `deliverable/slides/eb-workshop.tex` (new).
- Definition of done: file compiles conceptually (preamble + `\begin{document}`
  + title + two section dividers + `\end{document}`); no placeholder frames for
  W1–W12 content yet. — **Met.** `\begin`/`\end` environment pairs and brace
  count were checked programmatically (3 balanced `frame` pairs: title page +
  2 dividers, 2 `center` pairs, braces net to 0); no local `pdflatex`/`xelatex`
  available in this environment to do a full binary compile, so this is a
  structural check, not a rendered-PDF check.
- Depends on: none.
- Notes for Codex: Confirmed with the user (2026-07-16) via AskUserQuestion:
  title = "Empirical Bayes: Theory and Application" (matches the Gu–Walters
  2022 NBER Methods Lecture naming, since this deck extends that lecture),
  subtitle = "Overview and Point Estimation (Normal–Normal Model)" (previews
  the two parts), author = "Yu-Chang Chen", date = August 26, 2026. Used the
  skill's default `orchid` preamble verbatim (no extra packages needed yet).
  Section headings use the exact Part 1 / Part 2 titles from `SESSION.md`'s
  Current Objective line. Divider frames are centered big-text placeholders,
  not `\tableofcontents` slides, to stay strictly within "no content slides."

### W1

- Status: `done`
- Goal: Open the workshop. Define EB in plain language and preview where it
  shows up (many noisy estimates, ranking, selection, heterogeneity,
  small-area estimates, teacher effects, firm effects, A/B testing). Motivate
  why EB has become more prominent in economics recently (large administrative
  datasets, many unit-specific parameters). No math.
- Inputs: [walters-2024-eb-methods-labor-economics.md](../references/walters-2024-eb-methods-labor-economics.md)
  (Introduction / "Main framing" section); [gu-walters-2022-nber-eb-methods-lecture-slides.md](../references/gu-walters-2022-nber-eb-methods-lecture-slides.md)
  (Motivation slide).
- Target files: `deliverable/slides/eb-workshop.tex` (drafted directly into
  the deck rather than as a separate outline, since W0's skeleton already
  exists).
- Definition of done: ~2 slides — (1) "what is EB" one-liner + the three EB
  objectives (learn the distribution, borrow strength, make decisions),
  (2) a preview list of today's examples that foreshadows W2–W7. — **Met.**
  Frame 1 ("What Is Empirical Bayes?") opens with the large-administrative-
  data / many-unit-specific-parameters motivation, then the one-liner
  definition, then the three objectives as a numbered list. Frame 2 ("A
  Preview of Today's Examples") has one bullet per W2–W7 in order (school
  value-added individual estimate → distribution of school quality →
  value-added as a regressor/attenuation → other unit types (judges, firms,
  doctors/hospitals, police) → firm discrimination ranking → A/B testing),
  without exposing internal task IDs to the audience.
- Depends on: W0.
- Notes for Codex: Kept concept-only, no formulas, per plan. No `\cite`
  commands used for the Kline-Rose-Walters / Azevedo et al. mentions — the
  project has no `.bib` file yet and `biblatex` is loaded without
  `\addbibresource`, so `\cite`/`\citep` would break compilation; used plain
  parenthetical author mentions instead (matches how the `references/` notes
  themselves cite in prose). Revisit if/when a `.bib` file is added.

### W2

- Status: `done`
- Goal: Introduce teacher/school value-added as the running example. Show how
  EB improves the estimate for a single unit ("borrowing strength" /
  shrinkage) — concept only, no formula yet.
- Inputs: [walters-2024-eb-methods-labor-economics.md](../references/walters-2024-eb-methods-labor-economics.md)
  (Section 2 intro, Boston value-added application); [gu-walters-2022-nber-eb-methods-lecture-slides.md](../references/gu-walters-2022-nber-eb-methods-lecture-slides.md)
  (Application 1 — School Value-Added, "Posterior Means" slide, VAM figures).
- Target files: slide draft.
- Definition of done: ~2 slides — (1) the problem (noisy per-school estimates),
  (2) the EB fix stated in words ("pull noisy estimates toward the group
  average, more so when the estimate is noisier") with the Boston VAM
  histogram/figure referenced as an illustration. — **Met, split into 3
  frames.** (1) "Running Example: School Value-Added" sets up what
  $\hat\alpha_j$ is and why smaller schools are noisier (this setup wasn't
  free — W1 never defined value-added, only referenced it in the preview
  list); (2) "The Problem: Noise Masquerades as Quality" states the raw-
  ranking pitfall (extremes are disproportionately small/noisy schools,
  overstated between-school variance, real stakes for school-choice/
  accountability uses); (3) "The EB Fix: Borrow Strength Across Schools"
  states the shrinkage fix in words (more shrinkage for noisier schools) and
  ends with a figure placeholder for the Boston VAM before/after-shrinkage
  histogram (sourced to Gu & Walters 2022 Application 1 "Posterior Means"
  slide; underlying result Angrist, Hull, Pathak & Walters 2017) since no
  image asset exists in the repo yet.
- Depends on: W0.
- Notes for Codex: This is the "individual unit" leg of EB's three objectives;
  keep it distinct from W3 (distributional leg). Split the 2-slide estimate
  into 3 because "the problem" needed its own framing (winner's-curse-style
  ranking distortion) separate from "the fix," and neither point should share
  a slide with the running-example setup. No `\cite` used (same reasoning as
  W1 — no `.bib` file yet); the figure is a placeholder box, not an embedded
  image, since `deliverable/slides/` has no figure assets — swap in the real
  screenshot from `references/Slides2.pdf` before the workshop.

### W3

- Status: `done`
- Goal: Same running example, different question — the *distribution* of
  teacher/school effects (how much does quality vary across schools?).
- Inputs: [walters-2024-eb-methods-labor-economics.md](../references/walters-2024-eb-methods-labor-economics.md)
  (Section 2, "mixing distribution" framing); [gu-walters-2022-nber-eb-methods-lecture-slides.md](../references/gu-walters-2022-nber-eb-methods-lecture-slides.md)
  ("Introducing G" and "The Philosophy of G" slides).
- Target files: slide draft.
- Definition of done: ~2 slides — (1) the "how much does quality vary"
  question and why raw variance overstates it (sampling noise), (2) the
  fixed-effects vs random-effects framing of `G` as an objective feature of
  the population, stated in words. — **Met, split into 3 frames.**
  (1) "How Much Does Quality Really Vary?" poses the aggregate-variance
  question and states in words why raw variance overstates the truth
  (same bias-correction idea as the individual-estimate case, one level up
  — no formula, per "no math"); (2) "Introducing $G$: The Population
  Distribution of Quality" gives $G$ its own frame since it's a distinct,
  load-bearing object (this is the "prior" Part 2 formalizes) rather than a
  sub-bullet; (3) "Fixed Effects or Random Effects? Same Question, Either
  Way" states the FE/RE reconciliation and flags that this "random effects"
  sense is unrelated to the panel-data correlated-effects worry, to avoid
  confusing an econometrics-literate audience.
- Depends on: W0.
- Notes for Codex: This is the "learn the distribution" leg of EB. Good spot
  for the deconvolved-density figure style (even though full deconvolution
  math is out of scope here) — **not added**: kept this card text-only since
  the point (raw variance overstates truth) doesn't need a figure to land,
  and W2 already has one figure placeholder pending a real asset; revisit if
  a deconvolved-density image becomes available before the workshop.

### W4

- Status: `done`
- Goal: Explain why using a noisy teacher-effect estimate as a regressor in a
  downstream analysis is problematic (attenuation bias from classical
  measurement error in a regressor), and how EB-shrunk estimates correct it.
- Inputs: [walters-2024-eb-methods-labor-economics.md](../references/walters-2024-eb-methods-labor-economics.md),
  subsection **"Shrinkage and downstream regression — attenuation bias
  (§2.3)"** (added under Section 2 in a research pass — has the attenuation
  derivation, the EB fix, the right-side-vs-left-side asymmetry rule of thumb,
  the pooled-κ practical variant for heteroskedastic `s_j`, and worked
  citation examples).
- Target files: slide draft.
- Definition of done: ~2–3 slides — (1) state the problem in words: plugging
  a noisy `θ̂_j` into `Z_j = β₀ + β₁θ_j + e_j` biases `β̂₁` toward zero
  (classical measurement error / attenuation), illustrated with the teacher
  value-added → adult outcomes example (Chetty, Friedman & Rockoff 2014b);
  (2) state the fix in words: regress on the EB posterior mean instead of the
  raw estimate — shrinking by the signal-to-noise ratio exactly undoes the
  attenuation; (3) optional memorable one-liner slide — "shrinkage on the
  right fixes bias, shrinkage on the left causes it" (contrast with Chetty &
  Hendren 2018's neighborhood-effects-as-dependent-variable regression, where
  the *unbiased* raw estimate, not the shrunk one, is what belongs on the
  left). — **Met, 3 frames, one per point.** (1) "A Pitfall: Using
  $\hat\theta_j$ as a Regressor" states the problem in words with the
  Chetty–Friedman–Rockoff (2014b) worked example; (2) "The EB Fix: Regress
  on the Posterior Mean, Not the Raw Estimate" states the fix in words plus
  the variance-cost caveat (fixes bias, doesn't restore full precision);
  (3) "Memorable Rule: Right Side Fixes Bias, Left Side Causes It" states
  the asymmetry and closes with the one-liner as a large centered pull-quote,
  contrasted with Chetty \& Hendren (2018)'s left-hand-side case.
- Depends on: W0.
- Notes for Codex: Keep this concept-level (no equations) per the Part 1 "no
  math" instruction — the derivation (eq. 29–31 in the source) is available in
  the reference note if a formula is wanted, but Part 1's job is the intuition
  and the memorable rule of thumb. Do not present the "leave-year-out"
  supplementary point in the reference note as sourced to Walters (2024) — it
  is flagged there as outside-chapter interpretive content (Chetty, Friedman
  & Rockoff 2014a/b); fine to mention briefly but attribute correctly if used.
  **Followed this**: the leave-year-out point and the pooled-$\kappa$
  heteroskedastic variant were both left out of the drafted frames — neither
  is needed for the ~3-slide concept-level treatment, and omitting them
  avoids the misattribution risk the note flagged.

### W5

- Status: `done`
- Goal: Broaden the running example beyond schools — show EB applies to any
  "many similar units" setting: judges, firms, managers, neighborhoods,
  doctors, hospitals, police officers.
- Inputs: [walters-2024-eb-methods-labor-economics.md](../references/walters-2024-eb-methods-labor-economics.md)
  (Introduction's list of value-added settings and citations — judges,
  hospitals, police officers, firms); [gu-walters-2022-nber-eb-methods-lecture-slides.md](../references/gu-walters-2022-nber-eb-methods-lecture-slides.md)
  (Motivation slide — firm-specific wage premia, neighborhood effects);
  [other-unit-effects-gallery.md](../references/other-unit-effects-gallery.md)
  (new supplementary research note — verified, structured entries for
  judges, firms, doctors/hospitals, and police, each with citation, method,
  headline finding, and a ready-made slide one-liner).
- Target files: slide draft.
- Definition of done: ~2 slides — a short "gallery" of unit types with one
  citation/example each. Recommended picks (see "Suggested W5 slide
  selection" in the new reference note): judges — Arnold, Dobbie & Yang
  (2018) bail bias; firms — Abowd, Kramarz & Margolis (1999) AKM or Card,
  Heining & Kline (2013); doctors/hospitals — Chan, Gentzkow & Yu (2022)
  radiologists or Doyle et al. (2015) hospitals; police — Gonçalves & Mello
  (2021). — **Met, 2 frames.** (1) "Beyond Schools: The Same Problem,
  Everywhere" states the common-thread framing (quasi-random assignment to a
  unit isolates a unit-specific effect = EB's Step 1) as the connecting
  sentence, then hands off to the gallery; (2) "A Gallery of Many-Unit
  Settings" is a single `booktabs` table (Setting / Study / Headline
  finding) with exactly the four recommended picks — Arnold-Dobbie-Yang
  (judges), Abowd-Kramarz-Margolis/AKM (firms), Chan-Gentzkow-Yu
  (doctors/hospitals), Gonçalves-Mello (police) — plus a closing line
  pointing forward to W6 (firm discrimination = "the EB step further" for
  one of these settings).
- Depends on: W0.
- Notes for Codex: Supplementary research pass is done — see
  `other-unit-effects-gallery.md` for full details, including a "common
  thread" framing (every example uses quasi-random assignment to isolate a
  unit effect, the same Step-1 building block as Walters' EB recipe) that
  can double as the slide's connecting sentence. Keep this slide light —
  it's a gallery, not a deep dive; the note's "backup/depth" papers
  (Frandsen-Lefgren-Leslie, Card-Heining-Kline, Doyle et al.) are optional
  and mainly there in case a follow-up question comes up. **Followed this**:
  none of the backup/depth papers or the methodological caveat entries
  (Frandsen-Lefgren-Leslie, Chan-Gentzkow-Yu's skill-vs-preference wrinkle)
  made it onto the slide itself — the gallery stayed to one paper per unit
  type as suggested; used `\c{c}` for "Gonçalves" rather than a raw UTF-8
  character in the `.tex`, since the preamble declares no
  `inputenc`/`fontenc` and the ASCII-escape form is safer across engines.

### W6

- Status: `done`
- Goal: Use the Kline–Rose–Walters employer discrimination study to introduce
  EB for *ranking/selection* — which firms discriminate, and how EB supports
  naming them with statistical confidence (concept only, defer FDR/q-value
  formulas).
- Inputs: [kline-rose-walters-2022-systemic-discrimination.md](../references/kline-rose-walters-2022-systemic-discrimination.md)
  (full note — headline results, concentration/Lorenz-curve findings, 23-firm
  detection result); [gu-walters-2022-nber-eb-methods-lecture-slides.md](../references/gu-walters-2022-nber-eb-methods-lecture-slides.md)
  (Application 2 slides — histograms, Lorenz curve, deconvolved densities).
- Target files: slide draft.
- Definition of done: ~3 slides — (1) the design and headline finding (2.1pp
  average gap, large between-firm heterogeneity), (2) the concentration
  finding (top-quintile firms responsible for ~46–56% of gaps; Lorenz curve
  figure), (3) the "23 of 108 firms flagged" ranking/detection result, stated
  as "EB lets us say which specific firms are likely discriminators." —
  **Met, 3 frames, one per point.** (1) "The Design: Auditing 108 Large
  Employers" covers the correspondence-experiment design, the 2.1pp average
  racial gap (statistically-indistinguishable-from-zero average gender gap),
  and the between-firm SD heterogeneity (racial ≈1.9pp, gender ≈2.7pp);
  (2) "How Concentrated Is Discrimination?" states the deconvolution logic
  in words and the Lorenz-curve concentration numbers (top quintile ≈46%
  of lost Black contacts, Gini≈0.40; ≈56% of gender gaps, Gini≈0.54), with
  a figure placeholder; (3) "23 of 108 Firms: Naming Names with Statistical
  Confidence" states the posterior-mean/fat-tail point and the FDR-based
  detection result in words, closing with the "average → specific firms
  with confidence" takeaway line from the task goal.
- Depends on: W0.
- Notes for Codex: Pull figures from the paper (deconvolved density, Lorenz
  curve) rather than redrawing — note in the slide draft which page/figure
  number to screenshot from `references/w29053.pdf`. **Done precisely**: ran
  `pdftotext -layout` on `references/w29053.pdf` and confirmed by reading
  the extracted page text (not guessed) that Figure 6 ("Deconvolution
  estimates of firm-level discrimination distributions") is on PDF page 55
  and Figure 7 ("Discrimination Lorenz curves") is on PDF page 56 — both
  cited by page number in frame (2)'s figure placeholder. Also cross-checked
  the Lorenz-curve numbers directly against Figure 7's on-page text (Gini
  0.394/top-20%-0.46 for race, top-20%-0.56 for gender), which match the
  reference note.

### W7

- Status: `done`
- Goal: Use Azevedo et al.'s A/B testing paper to show EB in a non-labor
  setting, and to introduce the idea that the *shape* of the prior (fat vs.
  thin tails) can change the recommended strategy, not just the estimates.
- Inputs: [azevedo-et-al-2020-ab-testing-fat-tails.md](../references/azevedo-et-al-2020-ab-testing-fat-tails.md)
  (full note — fat vs. thin tail result, "top 2% of ideas generate 74.8% of
  gains," lean vs. big-data experimentation).
- Target files: slide draft.
- Definition of done: ~3 slides — (1) the setup (screening many ideas with
  scarce experimental users), (2) the fat-tail finding at Bing and what it
  implies (shrink small-t results hard, trust the outliers), (3) the
  "lean vs. big" experimentation takeaway and the ~17% productivity gain
  counterfactual. — **Met, 3 frames, one per point.** (1) "The Setup:
  Screening Many Ideas With Scarce Experiments" states the allocation
  problem and the ship-iff-posterior-mean-positive decision rule, tying it
  back to EB's "make decisions" objective from W1; (2) "The Fat-Tail
  Finding at Bing" states the fat-tail evidence and the two worked
  shrinkage examples ($t\approx2$: 0.044→0.006; $t\approx4$: 0.088→0.066),
  plus the top-2%-generates-74.8%-of-gains concentration stat;
  (3) "Lean vs.\ Big: How Fat Tails Change the Strategy" states the
  thin-vs-fat-tail strategy contrast and the ~17% productivity counterfactual
  from testing 20% more ideas on the same budget.
- Depends on: W0.
- Notes for Codex: Keep this concept-level; do not introduce the Student-t
  prior or characteristic-function identification argument here (that's out
  of scope for a no-math overview section). **Followed this**: neither the
  Student-t parametric-prior choice nor the characteristic-function
  deconvolution argument appears on the slides — the fat-tail result is
  stated purely as an empirical finding and its two decision consequences
  (aggressive shrinkage of small t-stats; lean vs. big strategy).

### W8

- Status: `done`
- Goal: Synthesize W1–W7 into a single "when is EB used" recap slide(s) that
  sets up the transition into Part 2's formal treatment.
- Inputs: no new source reading — pull the one-line takeaway from each of
  W1–W7's target notes.
- Target files: slide draft.
- Definition of done: ~1–2 slides listing the recurring pattern across all
  examples (many noisy unit-level estimates → borrow strength → better
  estimates/rankings/decisions) and a short bullet per example already
  covered. — **Met, 2 frames.** (1) "The Recurring Pattern: Same Three
  Objectives, Seven Examples" restates the pooling → sharpen/decide pattern
  in words, then a `booktabs` table mapping W1's three EB objectives (learn
  the distribution / improve individual estimates / support decisions) back
  onto which of W2–W7 exemplified each — several examples appear under more
  than one objective (W6 and W7 each span two); (2) "Today's Examples,
  Revisited" is a compact one-bullet-per-example recap (W2–W7, past tense,
  mirroring W1's preview-list frame structure but now stating the finding
  instead of previewing it), closing with a one-line transition into Part 2.
- Depends on: W1, W2, W3, W4, W5, W6, W7 (draft this last within Part 1). —
  all seven were done before this card was started, so the recap's content
  is accurate as written.
- Notes for Codex: This is a pure synthesis slide — write it only after the
  other Part 1 cards exist so the recap is accurate. Kept the transition
  line at the end of frame 2 intentionally thin ("Part 2 makes it precise,
  starting from the simplest possible case") — the actual bridge content
  (restating the running example with the sampling-model notation, the
  three-step EB recipe preview) is W9's separate job, not W8's; duplicating
  it here would step on W9's card.

### W9

- Status: `done`
- Goal: Bridge from "EB is useful" (Part 1) into "here's the simplest version
  of EB" (Part 2) — introduce the normal/normal model at a light, intuitive,
  example-driven level. This should track roughly the first half-hour of the
  Gu–Walters 2022 NBER Methods Lecture video/deck.
- Inputs: [gu-walters-2022-nber-eb-methods-lecture-slides.md](../references/gu-walters-2022-nber-eb-methods-lecture-slides.md)
  (Application 1 slides through "Normal/Normal Model" and "Posterior Means" —
  stop before "When to Shrink?"); [walters-2024-eb-methods-labor-economics.md](../references/walters-2024-eb-methods-labor-economics.md)
  (Section 2.1, "An Empirical Bayes Recipe").
- Target files: slide draft.
- Definition of done: ~3–4 slides — (1) restate the Boston schools example
  with the sampling model `θ̂_j | θ_j ~ N(θ_j, s_j²)` introduced informally,
  (2) the second-level model `θ_j ~ G` and the normal/normal special case,
  (3) the three-step EB recipe (estimate → deconvolve → posterior) stated as
  a preview, (4) explicit hand-off line to Part 2 ("now let's derive this"). —
  **Met, 4 frames, one per point.** (1) "Back to Boston Schools: The
  Sampling Model" restates the shared first step across every W2–W7 example
  and states $\hat\theta_j \mid \theta_j, s_j \sim N(\theta_j, s_j^2)$ as a
  display equation with one sentence of justification (CLT with enough
  observations per unit), grounded back in the Boston schools numbers;
  (2) "The Second Level: $\theta_j \sim G$" restates $G$ from W3 and states
  the normal/normal special case $\theta_j \sim N(\mu, \tau^2)$;
  (3) "Preview: The Three-Step EB Recipe" states estimation/deconvolution/
  posterior-formation as a numbered list, explicitly mapping deconvolution
  and posterior formation back to W1/W8's "learn the distribution" and
  "improve individual estimates" objectives; (4) "Now Let's Derive It" is
  the explicit hand-off, previewing Part 2's three-part roadmap (derive the
  posterior mean; estimate $\mu,\tau^2$ from data; explain why shrinkage
  helps on average).
- Depends on: W8 (comes right after the wrap-up in the agenda). — W8 was
  done before this card was started.
- Notes for Codex: Keep derivations light here — this is the "example-driven"
  pass; full derivation is W10's job. Avoid duplicating W10's content.
  **Followed this**: no algebra, no posterior-mean formula appears anywhere
  in these four frames — only the two defining distributional statements
  (sampling model, second-level model) and a prose preview of what's coming.
  Also note: this is the first point in the deck where light notation
  appears (Part 1 proper, W1–W8, was kept strictly "no math" per those
  cards' instructions) — deliberate, since introducing notation is exactly
  this card's job. Unified notation to the general $\theta_j$ (matching
  W4's regressor-pitfall notation and Part 2's upcoming usage) rather than
  W2/W3's school-specific $\alpha_j$, with an explicit sentence noting the
  switch is just relabeling, not a new example.
- **Placement note**: inserted as the last Part 1 content, immediately
  before the existing Part 2 section-divider frame (matches the Active
  Sequence table's "Part 1 #9" label and the 09:00–09:40 time-block
  breakdown in the "Rough slide-count total" note) — not after the divider.
  Frame 4's hand-off line now lands right before the audience sees the
  "Part 2: Point Estimation" title card, which reads as a clean pause point.

### W10

- Status: `todo`
- Goal: Full normal/normal setup with a simple worked derivation — sampling
  distribution, prior, and the posterior mean formula.
- Inputs: [gu-walters-2022-nber-eb-methods-lecture-slides.md](../references/gu-walters-2022-nber-eb-methods-lecture-slides.md)
  ("Normal/Normal Model" and "Posterior Means" slides — has the formula
  `θ*_j = [τ²/(τ²+s_j²)]θ̂_j + [s_j²/(τ²+s_j²)]μ`); [walters-2024-eb-methods-labor-economics.md](../references/walters-2024-eb-methods-labor-economics.md)
  (Section 2.1–2.2 for the fuller derivation/exposition).
- Target files: slide draft.
- Definition of done: ~4–5 slides — (1) sampling distribution
  `θ̂_j | θ_j, s_j ~ N(θ_j, s_j²)`, (2) prior `θ_j ~ N(μ, τ²)`, (3) the
  posterior-mean derivation (can be a single "algebra" slide or split into
  setup + result), (4) a picture showing the posterior mean as a
  precision-weighted average / shrinkage toward `μ`, (5) plain-language
  restatement of what the formula says.
- Depends on: W9.
- Notes for Codex: "簡單推導" — keep the derivation short (complete the
  square / precision-weighting argument), not a full measure-theoretic proof.

### W11

- Status: `todo`
- Goal: The "empirical" step — show how the prior's hyperparameters `(μ, τ²)`
  are estimated from the ensemble of units, turning the Bayes posterior mean
  into the EB posterior mean.
- Inputs: [gu-walters-2022-nber-eb-methods-lecture-slides.md](../references/gu-walters-2022-nber-eb-methods-lecture-slides.md)
  ("Estimating Hyperparameters" and "EB Posterior Means" slides — has
  `μ̂ = mean(θ̂_j)`, `τ̂² = mean[(θ̂_j−μ̂)²] − s_j²`); [walters-2024-eb-methods-labor-economics.md](../references/walters-2024-eb-methods-labor-economics.md)
  (Section 2.1 hyperparameter estimation discussion).
- Target files: slide draft.
- Definition of done: ~3–4 slides — (1) motivate: in practice we don't know
  `μ, τ²`, (2) method-of-moments estimators `μ̂`, `τ̂²`, with the bias-
  correction (subtracting `s_j²`) explained in words as "removing sampling
  noise," (3) the plug-in EB posterior mean formula, (4) a picture contrasting
  raw estimates vs. EB posterior means (e.g., the Boston VAM histogram before/
  after shrinkage).
- Depends on: W10.
- Notes for Codex: Briefly mention MLE and the Kline–Saggio–Sølvsten (2020)
  unbiased variance estimator as alternatives, per the source slide, without
  deriving them.

### W12

- Status: `todo`
- Goal: Introduce the James–Stein phenomenon and use it to build the
  intuition that shrinkage reduces *aggregate* risk, even though it can be
  worse for any single unit.
- Inputs: [gu-walters-2022-nber-eb-methods-lecture-slides.md](../references/gu-walters-2022-nber-eb-methods-lecture-slides.md)
  (the two "When to Shrink?" slides — single-unit vs. many-unit MSE
  comparison); [walters-2024-eb-methods-labor-economics.md](../references/walters-2024-eb-methods-labor-economics.md)
  ("James–Stein justification" point in Section 2 summary).
- Target files: slide draft.
- Definition of done: ~4–5 slides — (1) pose the question "should we prefer
  the shrunk estimate to the raw one?", (2) single-unit MSE comparison (raw
  `= s_j²`; shrunk has a bias term) — ambiguous for one unit, (3) many-unit
  MSE (integrated over `G`) — shrinkage wins, stated as the James–Stein
  result, holding regardless of normality, (4) a picture illustrating
  aggregate risk reduction (e.g., a stylized risk-vs-truth plot or the
  standard "baseball batting averages" style illustration if one is easy to
  source), (5) one-line intuition takeaway: "you don't have to believe the
  units are literally random draws for shrinkage to help on average."
- Depends on: W11.
- Notes for Codex: Keep the James–Stein *theorem* statement brief and
  intuitive per the outline ("放在本節簡短處理") — this is a risk-intuition
  slide, not a proof.

## Toy Demo Notes

You can test the automation with:

```bash
make codex-task-next
make codex-task-next
make codex-task-next
```

Expected result:

- `toy-demo.md` is updated in three small steps
- `TASKS.md` moves from `todo` to `done`
- `SESSION.md` keeps the handoff current after each run
