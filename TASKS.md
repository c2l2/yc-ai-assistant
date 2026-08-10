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
| W3 | done | Part 1 #3 — Teacher value-added: distribution of teacher effects. | Slide draft | See task card W3. Drafted as 3 slides, **compressed to 2 on 2026-07-17** (fixed/random-effects frame folded into "Introducing G" as one bullet). |
| W4 | done | Part 1 #4 — Teacher value-added: using the teacher effect as a regressor (attenuation bias + EB fix). | Slide draft | See task card W4. Drafted as 3 slides, **compressed to 2 on 2026-07-17** (Memorable Rule folded into the EB Fix frame's closing bullet + emphasis box). |
| W5 | done | Part 1 #5 — Other unit types: judge effects, firm effects, and the general "many units" list. | Slide draft | See task card W5. Drafted as 2 slides, **compressed to 1 on 2026-07-17** (Beyond Schools intro folded into the Gallery table frame). |
| W6 | done | Part 1 #6 — Ranking application: Kline–Rose–Walters discrimination study. | Slide draft | See task card W6. Drafted as 3 slides (matches the ~3 estimate). |
| W7 | done | Part 1 #7 — A/B testing application: Azevedo et al. fat tails. | Slide draft | See task card W7. Drafted as 3 slides (matches the ~3 estimate). |
| W8 | done | Part 1 #8 — Wrap-up: when is EB used (synthesis slide). | Slide draft | See task card W8. Drafted as 2 slides, **compressed to 1 on 2026-07-17** (Today's Examples Revisited bullet list dropped; table frame kept, its transition line appended). |
| W9 | done | Part 1 #9 — Bridge: introduce the simplest EB (normal/normal), example-driven, light touch. | Slide draft | See task card W9. Drafted as 4 slides, **compressed to 3 on 2026-07-17** (Now Let's Derive It folded into the Recipe Preview frame's closing paragraph). |
| W10 | done | Part 2 #1 — Normal/normal setup: sampling distribution, prior, posterior mean derivation. | Slide draft | See task card W10. Drafted as 5 slides (top of the ~4–5 estimate, per the user's explicit "setup + result + picture + plain-language" structure). |
| W11 | done | Part 2 #2 — From Bayes to Empirical Bayes: estimating hyperparameters from data. | Slide draft | See task card W11. Drafted as 5 slides (one above the ~3–4 estimate — each derivation step got its own frame with a plain-language gloss, per the user's explicit instruction). |
| W12 | done | Part 2 #3 — James–Stein phenomenon and the shrinkage-reduces-risk intuition. | Slide draft | See task card W12. Drafted as 5 slides (top of, not beyond, the ~4–5 estimate — kept brief per the user's explicit "簡短處理" instruction for this card). **Deck is now content-complete: W0–W12 all done.** |

Slide-count total (updated 2026-07-17 after drafting W12 — **deck is now
content-complete**): title + skeleton dividers (2) + Part 1 content
(**21** slides, compressed down from 26 — see "Part 1 Compression Pass"
below) + W10 (**5** slides) + W11 (**5** slides) + W12 (**5** slides) =
**38 frames total** — confirmed via `grep -c '\begin{frame}'`. No more
content cards remain in the queue; what's left is a real compile pass and
figure-asset collection (see W9/W10/W11's `SESSION.md` "Open Blockers").

## Part 1 Compression Pass (2026-07-17)

Part 1 ran long at 26 slides for a 09:00–09:40 block, so five pairs of
frames were merged down to 21 (still one frame per task-card content point,
just fewer *separate* frames for points that could share a slide):

- W8: "The Recurring Pattern" (table) + "Today's Examples, Revisited"
  (bullet recap) → one frame, table version kept, closing transition line
  appended after the table.
- W4: "The EB Fix: Regress on the Posterior Mean" + "Memorable Rule" → one
  frame; the rule-of-thumb mnemonic now closes the fix frame as a
  `\fcolorbox` emphasis box.
- W3: "Fixed Effects or Random Effects?" condensed from a full frame into
  one closing bullet on "Introducing $G$".
- W5: "Beyond Schools" opening frame folded into "A Gallery of Many-Unit
  Settings" as a lead-in paragraph before the table.
- W9: "Now Let's Derive It" folded into the end of "Preview: The
  Three-Step EB Recipe" as a closing paragraph.

No content points were dropped, only re-homed onto an existing slide;
task-card "Definition of done" text for W3/W4/W5/W8/W9 still describes the
original point-by-point content, now delivered across fewer frames — see
each card's notes for the specific merge.

## Revision Round 1 (Teacher Feedback, 2026-08-10)

The teacher reviewed the content-complete W0–W12 deck and gave a new round of
revision notes. These are tracked separately from the W0–W12 sequence (which
stays as historical record of how the deck was first drafted) using an `R`
prefix. **Planning/queue stage only — do not start drafting content until the
user explicitly approves individual task cards**, same rule as the original
Active Sequence.

**Status (2026-08-10): all of R1–R6 are `done` — this revision round is
complete.** Deck is at 44 frames, up from W0–W12's content-complete 38 (+5 R2,
-3 R3, +2 R4a, +0 R4b — R4b only added figures inside existing frames; R6
touched existing frames only, no frame-count change). Three sizing passes were
done across the session (see R4a's and R4b's card notes) to enlarge and
eventually unify this round's new figures. R6 is the compile-verification
pass those sizing passes were waiting on: it found and fixed 5 real content-
overflow frames (not just visual crowding) via a local `pdflatex` compile
loop, and separately discovered and repaired an unrelated file corruption
(see R6's card) — see R6 below for the full list.

| ID | Status | Task | Output / Deliverable | Notes |
| --- | --- | --- | --- | --- |
| R1 | done | Sweep the deck for audience-facing internal task-ID leaks (`W2`, `W3`, `W4`, `W9`, `W10`, etc.) and replace with descriptive, no-numbering phrasing. | Edits to `deliverable/slides/eb-workshop.tex` | See task card R1. Fixed 2026-08-10 — 6 remaining audience-facing spots reworded; only `%`-comment authoring notes still contain `W\d+` tokens. Re-verified 2026-08-10 after R2's five new frames landed — zero new leaks. |
| R2 | done | Insert a new "quick paper overview" mini-section between "A Preview of Today's Examples" and the deep-dive content, one card per paper. | New slides in `eb-workshop.tex` | Parent task — done 2026-08-10, 5 new frames (1 lead-in + R2a–R2d, 1 frame each). See R2a–R2d for the four paper-specific sub-cards. |
| R2a | done | Paper overview: teacher value-added main literature (Angrist–Hull–Pathak–Walters / Walters 2024 framing). | 1 slide | See task card R2a. |
| R2b | done | Paper overview: judge/firm effects gallery literature. | 1 slide | See task card R2b. |
| R2c | done | Paper overview: Kline–Rose–Walters (ranking/discrimination). | 1 slide | See task card R2c. |
| R2d | done | Paper overview: Azevedo et al. (A/B testing, fat tails). | 1 slide | See task card R2d. |
| R3 | done | Review and trim the formula/technical-detail slides bridging Part 1 into Part 2 (sampling model, normal/normal setup), keeping only what's essential. | Edits to `eb-workshop.tex` (W9/W10 region) | See task card R3. Done 2026-08-10 — 8 frames merged down to 5 (approved by user before editing). |
| R4 | todo | Re-review existing Part 1 slides against the "many pictures, light text, story-driven, example-led" style; simplify or split text-heavy/crowded frames. | Edits to `eb-workshop.tex` (Part 1 frames) | Parent task — see R4a/R4b for the two sub-passes. |
| R4a | done | Style pass, Part 1 first half (opening + teacher value-added: individual estimate, distribution, regressor pitfall). | Edits to `eb-workshop.tex` | See task card R4a. Done 2026-08-10 — 9-item list proposed, approved with 2 tweaks, all executed. **Paused here per user request — R4b awaits sign-off on the 3 new figures' style before starting.** |
| R4b | done | Style pass, Part 1 second half (other unit types, ranking, A/B testing, synthesis). | Edits to `eb-workshop.tex` | See task card R4b. Done 2026-08-10 — 8-frame list proposed, approved wholesale, all executed. **Revision round R1-R5 is now fully complete.** |
| R5 | done | Add more intuitive pictures to Part 2. | New figures + slides in `eb-workshop.tex` | Parent task — done 2026-08-10, 2 new TikZ frames inserted between W10 and W11. See R5a/R5b. |
| R5a | done | New figure: scatterplot of raw estimate (x-axis) vs. shrunk/posterior estimate (y-axis). | New figure + slide | See task card R5a. |
| R5b | done | New figure: schematic showing shrinkage magnitude vs. sample size. | New figure + slide | See task card R5b. |
| R6 | done | Local `pdflatex` compile pass to fix 5 frames with genuine content overflow (not just visual crowding) left over from the three prior sizing passes, without changing any bullet/figure content. | Edits to `eb-workshop.tex` | See task card R6. Done 2026-08-10 — also found and repaired an unrelated file corruption (chat instruction text had been pasted into the middle of a frame title). |

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
- **2026-07-17 figure-asset pass**: the `\fcolorbox` placeholder is now a
  real image, `deliverable/slides/figures/gu-walters-posterior-means.png`.
  Note this required a correction mid-task: the user first asked for
  `references/Slides2.pdf` page 12 ("Posterior Means"), but rendering that
  page showed it has **no chart at all** — just the frame title, three
  bullets, and the closed-form posterior-mean formula. Scanned every page
  in the deck via PyMuPDF's `get_images()`/`get_drawings()` counts to find
  pages that actually contain a rendered chart, then visually confirmed
  candidates; page 20, "Posterior Means Pooling Sectors," was the one that
  actually overlays raw BPS/Charter VAM estimates (outlined bars) with EB
  posterior means (filled bars) and the fitted prior curve — exactly the
  before/after-shrinkage comparison this card and W11 both describe. Asked
  the user to confirm before proceeding (page 20 vs. page 18's raw-only
  histogram vs. looking further); user picked page 20. Rendered at 6x zoom
  and cropped to the plot + axis label + legend only (title row and
  footer row excluded, no page-number text on this slide to worry about).
  This same file is now reused by W11 rather than creating a second,
  near-duplicate image (matches W11's card note about reusing this asset).
- **2026-07-18 sizing fix**: the user asked to shrink this frame's
  `\includegraphics` from `width=0.62\textwidth` down to
  `width=0.36\textwidth` (their message described the prior width as
  `0.5\textwidth` — the file actually had `0.62\textwidth`; applied the
  requested `0.36\textwidth` target regardless, noted here for the
  record). Nothing else on the frame changed. Note W11's frame
  ([Picture: Raw Estimates vs. EB Posterior Means], line ~833) still
  `\includegraphics`s the same PNG at `width=0.62\textwidth` — left
  untouched since the user's instruction named only this W2 frame.

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
- **2026-07-17 compression pass**: down to 2 frames. The "Fixed Effects or
  Random Effects?" frame no longer stands alone — its point is now the
  closing bullet on "Introducing $G$". Content unchanged, just re-homed;
  see `deliverable/slides/eb-workshop.tex`'s W3 comment block.

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
- **2026-07-17 compression pass**: down to 2 frames. The "Memorable Rule"
  frame no longer stands alone — its rule-of-thumb bullet and pull-quote now
  close out "The EB Fix: Regress on the Posterior Mean" frame (the quote is
  now an `\fcolorbox` emphasis box). Content unchanged, just re-homed; see
  `deliverable/slides/eb-workshop.tex`'s W4 comment block.

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
- **2026-07-17 compression pass**: down to 1 frame. The "Beyond Schools:
  The Same Problem, Everywhere" frame no longer stands alone — its
  common-thread text is now the lead-in paragraph on "A Gallery of
  Many-Unit Settings", right before the table. Content unchanged, just
  re-homed; see `deliverable/slides/eb-workshop.tex`'s W5 comment block.

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
- **2026-07-17 figure-asset pass**: the frame (2) `\fcolorbox` placeholder
  is now a real image. Rendered PDF pages 55-56 of `references/w29053.pdf`
  to PNG via PyMuPDF (`fitz`, 3x zoom), cropped each to just the
  title+plot+axis-label region (dropped the dense "Notes:" methodology
  paragraph and the rotated page-number margin -- neither belongs on a
  slide), and saved as `deliverable/slides/figures/kline-rose-walters-fig6.png`
  (Figure 6, 2209x965px) and `.../fig7.png` (Figure 7, 1364x1204px). Frame
  now shows both side by side via `\includegraphics` (`width=0.52\textwidth`
  for fig6, `width=0.26\textwidth` for fig7, chosen so the two render at
  roughly matching heights given their different native aspect ratios)
  with a small source citation line underneath, replacing the placeholder
  box entirely.

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
- **2026-07-18 figure-asset pass**: frame (2), "The Fat-Tail Finding at
  Bing," had no figure at all (unlike W2/W6/W10/W12, this card's original
  draft never flagged a placeholder) — the user asked specifically for one
  to be added. Confirmed the right source figure by reading
  `references/azevedo-et-al-ab.pdf` via `pdftotext -layout` rather than
  guessing: Figure 1, "The posterior mean function
  $P_i(\hat\delta_i, n_i)$," is on PDF page 9, and the paper's own text
  (p.25, Section 4.6.1) walks through this exact figure using the same two
  numbers already on this slide (0.044→0.006 at $t\approx2$; 0.088→0.066 at
  $t\approx4$) — a direct match, not just a thematic one. Candidates
  considered and ruled out: Figure 4 (p.21, log-log tail plots — illustrates
  fat-tailedness generally but not the shrinkage story) and Figure 3 (p.20,
  histogram/Q-Q model fit — about goodness-of-fit, not shrinkage). Rendered
  page 9 via PyMuPDF (`fitz`, 4x zoom) and cropped to just the plot + axis
  labels (dropped the page-number margin, the "Figure 1:" caption line, the
  "Notes:" methodology paragraph, and the surrounding body text) — saved as
  `deliverable/slides/figures/azevedo-fig1-posterior-mean.png` (1130×720px).
  Condensed the frame's bullets from 4 to 3 (merged the shrinkage-numbers
  bullet and the closing "shape of the prior" bullet into one, since both
  describe the same figure) to make room, then added the image at
  `width=0.4\textwidth` with a source citation line, following the same
  `\vs` + `center` + `\includegraphics` + `{\scriptsize Source: ...}`
  pattern used by W2/W6/W11. No local `pdflatex`/`xelatex` available to
  visually confirm the layout — structural check only (brace balance 494/494,
  `frame`/`center`/`itemize` environment pairs all balanced, frame count
  unchanged at 38 since this added content to an existing frame, not a new
  one).
- **2026-07-18 sizing/spacing fix**: user asked to shrink the image further
  and tighten the gap above it. Changed `\includegraphics[width=0.4\textwidth]`
  to `width=0.25\textwidth`, and replaced the `\vs` (`\vspace{1em}`) between
  the bullet list and the `center` block with `\vspace{0.3em}`. The gap
  between the image and its caption line (a blank line inside `center`)
  was left untouched, per the user's instruction. Bullets unchanged.

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
- **2026-07-17 compression pass**: down to 1 frame. "Today's Examples,
  Revisited" (the per-example bullet recap) was dropped as redundant with
  the table already on frame 1 — only its closing transition sentence
  ("Every one of these examples ran on intuition alone...") survived,
  appended after the table. See `deliverable/slides/eb-workshop.tex`'s W8
  comment block.

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
- **2026-07-17 compression pass**: down to 3 frames. "Now Let's Derive It"
  (frame 4, the explicit hand-off) no longer stands alone — it's now the
  closing paragraph of frame 3 ("Preview: The Three-Step EB Recipe"), right
  after "now we make it precise." The hand-off still lands immediately
  before the Part 2 section divider, just without its own slide. See
  `deliverable/slides/eb-workshop.tex`'s W9 comment block.

### W10

- Status: `done`
- Goal: Full normal/normal setup with a simple worked derivation — sampling
  distribution, prior, and the posterior mean formula.
- Inputs: [gu-walters-2022-nber-eb-methods-lecture-slides.md](../references/gu-walters-2022-nber-eb-methods-lecture-slides.md)
  ("Normal/Normal Model" and "Posterior Means" slides — has the formula
  `θ*_j = [τ²/(τ²+s_j²)]θ̂_j + [s_j²/(τ²+s_j²)]μ`); [walters-2024-eb-methods-labor-economics.md](../references/walters-2024-eb-methods-labor-economics.md)
  (Section 2.1–2.2 for the fuller derivation/exposition).
- Target files: `deliverable/slides/eb-workshop.tex`.
- Definition of done: ~4–5 slides — (1) sampling distribution
  `θ̂_j | θ_j, s_j ~ N(θ_j, s_j²)`, (2) prior `θ_j ~ N(μ, τ²)`, (3) the
  posterior-mean derivation (can be a single "algebra" slide or split into
  setup + result), (4) a picture showing the posterior mean as a
  precision-weighted average / shrinkage toward `μ`, (5) plain-language
  restatement of what the formula says. — **Met, 5 frames** (top of the
  ~4–5 estimate, per the user's explicit request to structure it as
  setup + derivation + result + picture + plain-language, and their
  instruction not to feel bound by the original estimate). (1) "Setting Up
  the Derivation: What We Know, What We Want" formally restates both
  distributions from W9 (Level 1 sampling model, Level 2 prior) as the
  derivation's starting point, states the target
  ($E[\theta_j \mid \hat\theta_j]$), and flags that `μ, τ²` are treated as
  known here (estimating them is W11's job); (2) "Deriving the Posterior
  Mean: Precision-Weighting" gives the short derivation — Bayes' rule,
  the completing-the-square/precision-adding argument — without a full
  measure-theoretic proof; (3) "Result: The Posterior Mean Formula" states
  the closed-form `θ*_j` formula plus the posterior-variance formula, and
  notes the EB version plugs in `(μ̂, τ̂²)`; (4) "Picture: Shrinkage as a
  Precision-Weighted Pull Toward `μ`" is a figure placeholder (`\fcolorbox`)
  for a schematic diagram (number line, `μ` at center, two example units'
  arrows of different lengths) — flagged explicitly as *to be drawn fresh*,
  not a paper screenshot, since no existing figure fits this exact
  illustration; (5) "What the Formula Says, in Plain Language" restates the
  formula in words (reliability weight, precise-vs-noisy limiting cases)
  and ties it back to the Part 1 shrinkage pictures the audience already
  saw without a formula (W2's VAM histogram, W4's attenuation-bias fix).
- Depends on: W9. — done, unaffected by the 2026-07-17 Part 1 compression
  pass (that pass changed W9's frame count, not its content or status).
- Notes for Codex: "簡單推導" — keep the derivation short (complete the
  square / precision-weighting argument), not a full measure-theoretic
  proof. **Followed this**: frame (2) states the precision-adding result
  as a general fact about combining Gaussian signals rather than working
  through the full algebra term-by-term; no measure theory, no general
  conjugate-prior theorem invoked. Structural check after drafting: brace
  balance and `\begin`/`\end` environment pairs still net to zero (checked
  programmatically, same method as prior turns); display-math `\[...\]`
  opens/closes balanced (4/4 across the whole file, 2 new from W10); total
  frame count 28 (`grep -c '\begin{frame}'`), consistent with 23 pre-W10 +
  5 new. Still no local `pdflatex`/`xelatex` — **not compiled**, structural
  check only; recommend the user compile in Overleaf to confirm before
  trusting the math typesets as intended.
- **2026-07-17 figure-asset pass**: frame (4)'s `\fcolorbox` placeholder is
  now a hand-drawn TikZ schematic (not a paper screenshot, per the card's
  own note that no existing figure fits this exact illustration). Added
  `\usepackage{tikz}` to the preamble (new package for this deck). The
  picture is a horizontal number line with `μ` marked and dashed at center,
  and two example units: unit `A` (small `s_j`, precise) has its raw
  estimate close to `μ` with a short arrow to its posterior mean; unit `B`
  (large `s_j`, noisy) has its raw estimate far from `μ` with a long arrow
  landing close to `μ` — open circles mark raw `\hat\theta_j`, filled
  circles mark shrunk `\theta_j^*`, arrow length visibly scales with
  shrinkage magnitude as the placeholder specified. Wrapped in
  `\resizebox{0.92\textwidth}{!}{...}` so it scales to fit regardless of
  the tikzpicture's native coordinate-space size, since there is no local
  compiler to check the raw size against the frame. Structural check after
  the edit (same method as every prior turn, redone carefully this time
  after an initial regex mistake double-counted `\\[0.4em]`-style
  line-break spacing as false display-math opens): brace balance nets to
  zero (478/478); all `\begin`/`\end` environment pairs balanced, including
  the new `tikzpicture` (1/1); frame count still 38 (unchanged — content
  was replaced inside an existing frame, no frame added/removed); real
  display-math `\[...\]` opens/closes correctly 8/8 once `\\[...]`
  linebreak-spacing false positives are excluded; dollar-sign count even
  (322). Still no local `pdflatex`/`xelatex` — **not compiled**; this is
  the first TikZ content in the deck, so an Overleaf compile pass is
  especially recommended next to confirm the coordinates/arrows render as
  intended (geometry was reasoned through, not visually verified).
- **2026-07-18 label-collision fix**: the `\mu` label and unit `B`'s
  `\theta_B^*` label sat almost on top of each other (unit `B`'s shrunk
  point lands very close to `\mu` by design), which the user caught when
  reviewing the frame. Moved `\mu`'s label from below the axis
  (`\node[below] at (0,-0.35)`) to above it (`\node[above] at (0,0.2)`),
  leaving `\theta_B^*` as the only label below the axis near that point.
  No coordinates, arrows, or colors changed — label position only.
- **2026-07-22 internal-ID wording fix**: frame (5), "What the Formula Says,
  in Plain Language," used the internal task codes "(W2)" and "(W4)" as if
  the audience had a numbering key to decode them — the deck exposes no such
  system to viewers. Changed to purely descriptive phrasing: "the Boston VAM
  histogram from earlier" and "the attenuation-bias fix you saw earlier."
  Wording only, no change to which examples are referenced.

### W11

- Status: `done`
- Goal: The "empirical" step — show how the prior's hyperparameters `(μ, τ²)`
  are estimated from the ensemble of units, turning the Bayes posterior mean
  into the EB posterior mean.
- Inputs: [gu-walters-2022-nber-eb-methods-lecture-slides.md](../references/gu-walters-2022-nber-eb-methods-lecture-slides.md)
  ("Estimating Hyperparameters" and "EB Posterior Means" slides — has
  `μ̂ = mean(θ̂_j)`, `τ̂² = mean[(θ̂_j−μ̂)²] − s_j²`); [walters-2024-eb-methods-labor-economics.md](../references/walters-2024-eb-methods-labor-economics.md)
  (Section 2.1 hyperparameter estimation discussion).
- Target files: `deliverable/slides/eb-workshop.tex`.
- Definition of done: ~3–4 slides — (1) motivate: in practice we don't know
  `μ, τ²`, (2) method-of-moments estimators `μ̂`, `τ̂²`, with the bias-
  correction (subtracting `s_j²`) explained in words as "removing sampling
  noise," (3) the plug-in EB posterior mean formula, (4) a picture contrasting
  raw estimates vs. EB posterior means (e.g., the Boston VAM histogram before/
  after shrinkage). — **Met, 5 frames** (one above the ~3–4 estimate — split
  per the user's explicit instruction this turn to keep the derivation steps
  but simplify the algebra, pairing each step with its own plain-language
  gloss rather than stacking formulas onto fewer slides). (1) "The Empirical
  Step: We Don't Actually Know $\mu$ and $\tau^2$" motivates the problem and
  ties it to W9's "deconvolution" step; (2) "Estimating $\mu$" gives
  `μ̂ = mean(θ̂_j)` with the unbiasedness intuition (noise averages out); (3)
  "Estimating $\tau^2$" gives the bias-corrected formula
  `τ̂² = raw variance − average(s_j²)` with an in-words gloss for each term
  and a truncate-at-zero caveat, naming MLE and Kline–Saggio–Sølvsten (2020)
  as alternatives without deriving them; (4) "From Bayes to Empirical Bayes:
  Plug and Play" substitutes `(μ̂, τ̂²)` into W10's formula, states this is
  the EB posterior mean, and explicitly closes W9's three-step recipe
  (estimation → deconvolution → posterior formation); (5) "Picture: Raw
  Estimates vs. EB Posterior Means" is a figure placeholder that
  **deliberately reuses** the figure-asset need already flagged for W2
  (Boston VAM before/after histogram) rather than creating a new, near-
  duplicate asset — the placeholder text says to caption it with the
  actual computed `μ̂, τ̂²` this time, making the same figure concrete
  instead of schematic.
- Depends on: W10. — done.
- Notes for Codex: Briefly mention MLE and the Kline–Saggio–Sølvsten (2020)
  unbiased variance estimator as alternatives, per the source slide, without
  deriving them. **Followed this**: both named in frame 3's caveat bullet,
  neither derived. Also followed this turn's explicit user instruction: no
  intermediate algebra shown for *why* raw variance decomposes into
  `τ² + average noise` (no law-of-total-variance derivation) — frame 3
  states the result formula directly and glosses each term in words instead.
  Structural check after drafting: brace balance and `\begin`/`\end` pairs
  still net to zero; display-math `\[...\]` opens/closes balanced (7/7,
  3 new from W11); dollar-sign count even (268); total frame count 33
  (`grep -c '\begin{frame}'`), consistent with 28 pre-W11 + 5 new. Still no
  local `pdflatex`/`xelatex` — not compiled, structural check only.
- **2026-07-17 figure-asset pass**: frame 5's `\fcolorbox` placeholder is
  now `\includegraphics` pointing at
  `deliverable/slides/figures/gu-walters-posterior-means.png` — the same
  file W2 now uses (per this card's own note above, "deliberately reuses"
  the asset rather than duplicating it). See W2's card for the sourcing
  detail: the user's initial page request (`Slides2.pdf` p. 12) had no
  chart on it; the correct chart (raw-vs-posterior histogram) turned out
  to be p. 20, "Posterior Means Pooling Sectors," confirmed with the user
  before cropping. The image already carries real computed numbers (std.
  dev. of estimates/prior/posterior means printed on the chart itself), so
  this satisfies the "caption with the actual computed values" goal
  without needing a separate re-caption — it's the real underlying figure,
  not a schematic with placeholder numbers.
- **2026-07-22 internal-ID wording fix**: two audience-facing bullets used
  bare task codes as if the audience could decode them. In frame 4, "From
  Bayes to Empirical Bayes: Plug and Play," "W9's three-step recipe" →
  "The three-step recipe from before," and "into W10's posterior mean
  formula" → "into the posterior mean formula from before." In frame 1,
  "The Empirical Step," "This is W9's ``deconvolution'' step" → "This is
  the ``deconvolution'' step." Wording only. **Not touched** (outside the
  user's explicit list for this pass): frame 1 still opens with "W10's
  posterior mean formula assumed..." — same bare-code issue, left for a
  follow-up pass if full within-frame consistency is wanted.

### W12

- Status: `done`
- Goal: Introduce the James–Stein phenomenon and use it to build the
  intuition that shrinkage reduces *aggregate* risk, even though it can be
  worse for any single unit.
- Inputs: [gu-walters-2022-nber-eb-methods-lecture-slides.md](../references/gu-walters-2022-nber-eb-methods-lecture-slides.md)
  (the two "When to Shrink?" slides — single-unit vs. many-unit MSE
  comparison); [walters-2024-eb-methods-labor-economics.md](../references/walters-2024-eb-methods-labor-economics.md)
  ("James–Stein justification" point in Section 2 summary).
- Target files: `deliverable/slides/eb-workshop.tex`.
- Definition of done: ~4–5 slides — (1) pose the question "should we prefer
  the shrunk estimate to the raw one?", (2) single-unit MSE comparison (raw
  `= s_j²`; shrunk has a bias term) — ambiguous for one unit, (3) many-unit
  MSE (integrated over `G`) — shrinkage wins, stated as the James–Stein
  result, holding regardless of normality, (4) a picture illustrating
  aggregate risk reduction (e.g., a stylized risk-vs-truth plot or the
  standard "baseball batting averages" style illustration if one is easy to
  source), (5) one-line intuition takeaway: "you don't have to believe the
  units are literally random draws for shrinkage to help on average." —
  **Met, 5 frames**, kept at the top of (not beyond) the ~4–5 estimate per
  the user's explicit "簡短處理，重點放直覺，不用完整證明" instruction for
  this card specifically. (1) "Should We Always Trust the Shrunk Estimate?"
  poses the question via risk/MSE framing; (2) "For One Unit, It's
  Ambiguous" gives one short display equation —
  `MSE(θ̂_j)=s_j²` vs. `MSE(θ̂*_j)=w_j²s_j²+(1-w_j)²(θ_j-μ)²` with
  `w_j=τ²/(τ²+s_j²)` — glossed in words (smaller variance, but a new bias
  term that can dominate for an atypical unit); (3) "But Averaged Across
  Many Units, Shrinkage Wins" states the aggregate result in words (no
  further algebra), names it the James–Stein phenomenon (James \& Stein
  1961), and notes it holds regardless of `G`'s normality (best *linear*
  predictor result) — explicitly declines to reprove the theorem; (4)
  "Picture: One Unit's Risk vs.\ Everyone's Risk" is a figure placeholder
  for a schematic risk-crossing plot tying frames 2 and 3 together visually
  (raw estimator flat risk line vs. shrunk estimator's crossing curve); (5)
  "The Takeaway" closes with the fixed/random-effects callback to W3 and a
  bold pull-quote emphasis box (mirroring W4's closing-box pattern), since
  this is the deck's last content frame.
- Depends on: W11. — done.
- Notes for Codex: Keep the James–Stein *theorem* statement brief and
  intuitive per the outline ("放在本節簡短處理") — this is a risk-intuition
  slide, not a proof. **Followed this**: frame 3 states the result and its
  normality-robustness in one bullet each, with an explicit "we won't
  reprove the theorem here" line; no measure theory, no minimax argument,
  no explicit integration-over-`G` algebra anywhere in the card. Structural
  check after drafting (same method as every prior turn): brace balance and
  `\begin`/`\end` pairs still net to zero; display-math `\[...\]`
  opens/closes balanced (8/8, 1 new from W12); dollar-sign count even
  (324); total frame count 38 (`grep -c '\begin{frame}'`), consistent with
  33 pre-W12 + 5 new. Still no local `pdflatex`/`xelatex` — not compiled,
  structural check only.
- **Deck-completion note**: this was the last `todo` content card in the
  queue. **W0–W12 are all `done`** — both Part 1 (21 slides) and Part 2
  (W10+W11+W12 = 15 slides) are now content-complete, 38 frames total. What
  remains is not more content drafting but (a) a real `pdflatex`/`latexmk`
  compile pass (never done in this environment — see `SESSION.md` "Open
  Blockers," recurring across W9–W12) and (b) collecting/designing the
  figure assets flagged throughout (W2, W6, W10, W12 all had `\fcolorbox`
  placeholders to replace with real images — **W2, W6, W10, and W11's
  reused copy of W2's figure are all done as of 2026-07-17**, see those
  cards' latest notes).
- **2026-07-18 figure-asset pass (W12's own turn, not a follow-up)**: the
  frame (4) `\fcolorbox` placeholder is now a hand-drawn TikZ risk-vs-
  distance plot, same treatment as W10's number-line schematic. Axes are
  `|θ_j-μ|` (x) vs. MSE (y); a flat gray line at constant height marks the
  raw estimator's risk `s_j^2`; a rising blue curve
  (`1 + 0.13x^2`, chosen only to look right at this frame's scale, not
  fit to real numbers) starts below the flat line near the origin and
  crosses above it further out, with the crossing point marked by a dot
  and a dashed drop-line, plus `<->` bracket labels underneath reading
  "shrinkage wins" / "raw wins" on either side of the crossing. This
  closes the deck's last open figure placeholder — **W0–W12 now have every
  figure done, no `\fcolorbox` placeholders remain anywhere in
  `eb-workshop.tex`.**
- **2026-07-18 sizing fix**: the user caught that `\resizebox{0.85\textwidth}`
  let this figure's content spill past the slide margins (wider aspect
  ratio than W10's number-line diagram, since this plot also has axis
  labels and the wins-brackets extending below the x-axis). Reduced to
  `\resizebox{0.6\textwidth}{!}` — the tikzpicture's internal coordinates,
  labels, and colors are untouched, only the overall scale shrank.
- **2026-07-22 internal-ID wording fix**: frame 5, "The Takeaway," said
  "recall W3's fixed-vs-random-effects point" — a bare task code with no
  audience-facing numbering key to decode it. Changed to "recall the
  earlier fixed-vs-random-effects point." Wording only.

## Revision Round 1 Task Cards

Detailed cards for the R-prefixed revision tasks above (teacher feedback,
2026-08-10). Same rule as the Workshop Task Cards: draft an outline first,
don't touch `eb-workshop.tex` until the user approves the individual card.

### R1

- Status: `done`
- Goal: Find every place in the slide body text (not code comments — those
  are fine to keep as authoring notes) where an internal task ID like `W2`,
  `W3`, `W4`, `W9`, `W10` etc. leaks into what the audience actually reads,
  and rewrite it as a plain descriptive reference with no numbering scheme
  ("the Boston VAM histogram from earlier," "the earlier fixed-vs-random-
  effects point," "the posterior mean formula from before").
- Inputs: `deliverable/slides/eb-workshop.tex` itself (grep for `W[0-9]+`
  inside `\begin{frame}...\end{frame}` bodies, not the `% ---` comment
  banners between frames).
- Target files: `deliverable/slides/eb-workshop.tex`.
- Definition of done: no `W\d+`-style token remains inside any frame's
  rendered text. — **Met.** A 2026-07-22 pass had already fixed four spots
  (see W10/W11/W12 card notes above); this pass (2026-08-10) fixed the six
  that remained: (1)/(2) "Setting Up the Derivation" frame, "(from W9)" and
  "(also from W9)" → "(as introduced earlier)" / "(also introduced
  earlier)"; (3) same frame, "Bayes formula, W11's job" → "Bayes formula,
  which comes next"; (4) "Result: The Posterior Mean Formula" frame,
  "exactly W11's job" → "exactly what comes next"; (5) "The Empirical Step"
  frame, "W10's posterior mean formula assumed" → "The posterior mean
  formula from before assumed" (this was the one the 2026-07-22 pass
  explicitly left unfixed); (6) "Estimating $\tau^2$" frame, "in Part 1
  (W3)" → "earlier"; (7) "For One Unit, It's Ambiguous" frame, "is W10's
  shrinkage weight" → "is the shrinkage weight from before". Re-grepped
  `W[0-9]+` afterward — every remaining match is inside a `%`-comment
  banner (authoring notes between frames), none inside a `\begin{frame}`
  body. Structural check: brace balance unchanged (495/495), frame count
  unchanged (38/38 `\begin{frame}`/`\end{frame}`) — wording-only edit, no
  layout risk.
- Depends on: none (pure find-and-reword, done independent of other R
  tasks). Note for future R2–R5 work: those tasks will add/move text and
  could introduce new `W\d+` leaks or shift line numbers — re-grep after
  each lands rather than assuming R1 covers content added later.
- Notes for Codex: Comments (`% --- W6: ... ---`) are internal authoring
  notes, not audience-facing — left alone, per plan. Only text inside
  `\begin{frame}...\end{frame}` bodies (bullet text, captions, footnotes)
  was touched.
- **2026-08-10 re-verification pass (after R2 landed)**: user asked to
  re-scan the whole deck since R2 added 5 new frames (including a new
  `% --- R2: ... ---` comment banner that itself mentions `W1`, `W5` while
  explaining the reuse decisions). Wrote a small script to walk the file
  line-by-line, skip any line starting with `%`, and flag `W\d+` matches
  only while inside a `\begin{frame}...\end{frame}` span — zero hits.
  Cross-checked with a plain `grep -n 'W[0-9]+'` and a `grep -n
  '\bR[0-9]+[a-d]?\b'` pass over the whole file: every match in both is
  inside a `%`-comment line (the original W1–W12 banners, plus the new R2
  banner's own internal cross-references). No `W\d+` or `R\d+` token
  leaked into any frame's rendered text. Confirms R2's drafting followed
  R1's rule correctly — no regression.

### R2a

- Status: `done`
- Goal: A "paper at a glance" slide (or two) for the teacher value-added
  literature underlying the W2/W3/W4 running example — research question,
  why EB is the right tool, and the main finding, with the finding shown as
  a figure/table wherever possible rather than prose.
- Inputs: [walters-2024-eb-methods-labor-economics.md](../references/walters-2024-eb-methods-labor-economics.md);
  figure to reuse: `deliverable/slides/figures/gu-walters-posterior-means.png`
  (already used by W2 and W11) — **user decision (2026-08-10): reuse this
  existing figure directly rather than drafting a new/simpler one.**
- Target files: new slide draft; eventual home in `eb-workshop.tex` between
  "A Preview of Today's Examples" and the first deep-dive frame.
- Definition of done: 1–2 slides with (a) the research question in one
  sentence, (b) a one-line "why EB" justification (many noisy unit-level
  estimates, need to separate signal from sampling noise), (c) the headline
  finding shown via the reused `gu-walters-posterior-means.png` figure. —
  **Met, 1 frame.** "Paper at a Glance: Teacher \& School Value-Added"
  states the research question (how much do teachers/schools differ, how
  to get a trustworthy per-unit estimate), the why-EB justification (raw
  estimates are noisy, especially for small schools, and confuse noise with
  real quality unless corrected), and the shrinkage finding, closing with
  `gu-walters-posterior-means.png` at `width=0.32\textwidth` (smaller than
  W2's `0.36\textwidth`, since this frame carries three bullets above it
  vs. W2's two-bullet-plus-figure layout).
- Depends on: none content-wise; sequencing depends on R2b–R2d for shared
  section framing (all four should read as one consistent "quick overview"
  mini-section, so drafting them together or immediately in sequence is
  recommended even though each is its own card).
- Notes for Codex: Keep this distinct from W2/W3/W4's later deep dives —
  this is a preview/orientation card, the deep dives still do the full
  walkthrough. Avoid duplicating content verbatim; this should feel like an
  abstract, not a rerun. Reusing the same image as W2/W11 means this will be
  its third appearance in the deck — fine per the user's explicit decision,
  but worth a caption/framing tweak so it doesn't feel like a verbatim
  repeat (e.g., overview slide shows it with less annotation/detail than
  the deep-dive frame). **Followed this**: no separate caption line/stats
  box was added here (W11's version does that); this frame's caption is
  just the one-line source citation, kept lighter than W2/W11's treatment.

### R2b

- Status: `done`
- Goal: A "paper at a glance" slide for the judge/firm-effects gallery
  literature (the W5 many-unit-types survey) — research question(s), why EB,
  main finding(s), visual where possible.
- Inputs: [other-unit-effects-gallery.md](../references/other-unit-effects-gallery.md).
- Target files: new slide draft; eventual home in `eb-workshop.tex` in the
  new overview mini-section.
- Definition of done: **user decision (2026-08-10): do NOT reuse W5's
  four-row gallery table here.** Instead, 1 slide (not 2) with a single
  one-line framing — "this same problem (many noisy unit-level estimates)
  shows up across judges, firms, doctors/hospitals, police, etc." — no
  table, no per-paper research-question/finding breakdown. The full table
  with citations stays exclusively on W5's deep-dive frame. — **Met.**
  "Paper at a Glance: Beyond Schools" is prose only, no bullets, no table,
  no figure: one sentence naming the four settings (judges, firms, doctors/
  hospitals, police) and framing EB as the general-purpose fix, plus one
  short transition sentence pointing forward to W5's fuller gallery.
- Depends on: none (see R2a's note on drafting all of R2a–R2d together for
  consistency).
- Notes for Codex: This card is the odd one out in the R2 set precisely
  because it's *not* a single-paper overview — per the user's explicit
  instruction, keep it to one short, punchy sentence/frame rather than
  trying to compress four studies into "why EB + main finding" format the
  way R2a/R2c/R2d do. Resist the urge to add a mini-table "just to be
  thorough" — that's the exact thing this decision was meant to avoid.
  **Followed this**: no itemize list, no table, no figure — just two
  sentences of running prose, the lightest frame in the whole mini-section.

### R2c

- Status: `done`
- Goal: A "paper at a glance" slide (or two) for Kline–Rose–Walters (used
  for the ranking/discrimination application, W6) — research question, why
  EB, main finding, visual.
- Inputs: [kline-rose-walters-2022-systemic-discrimination.md](../references/kline-rose-walters-2022-systemic-discrimination.md);
  figures to reuse: `deliverable/slides/figures/kline-rose-walters-fig6.png`
  and `.../fig7.png` — **user decision (2026-08-10): reuse these existing
  figures directly rather than drafting simplified versions.**
- Target files: new slide draft; eventual home in `eb-workshop.tex` overview
  mini-section.
- Definition of done: 1–2 slides — research question (do specific firms
  discriminate, and can we name them with confidence?), why EB (average
  effect is small/noisy per firm, need to separate real heterogeneity from
  sampling noise before ranking), and the headline finding shown via the
  reused fig6/fig7 images (concentration/Lorenz result and/or the "23 of
  108 firms" result). — **Met, 1 frame.** "Paper at a Glance: Which Firms
  Discriminate?" states the research question (even spread vs. concentrated
  discrimination, naming firms with confidence), the why-EB justification
  (each firm's audit estimate is noisy on its own; EB deconvolves the true
  distribution and controls the false discovery rate for flagging), and the
  headline concentration + "23 of 108" findings, closing with both fig6 and
  fig7 side by side (kept the pair, per the "use judgment" note below) at
  `width=0.42\textwidth`/`0.21\textwidth` — same 2:1 ratio as W6's
  `0.52`/`0.26`, scaled down to fit under three bullets.
- Depends on: none (see R2a's note).
- Notes for Codex: Same third-appearance consideration as R2a — fig6/fig7
  will now appear on both the overview slide and W6's deep dive, which is
  fine per the user's explicit decision; if both figures together feel like
  too much for a "quick" overview slide, it's fine to use just one of the
  two here (e.g., fig7's Lorenz curve alone) and keep the pair for W6 —
  use judgment, but don't switch to a different (non-reused) visual without
  checking with the user first. **Followed this**: kept both fig6 and fig7
  (matching the user's literal "KRW Figure 6/7" instruction rather than
  trimming to one) — revisit if a compile pass shows the pair too cramped
  next to three bullets of text on one frame.

### R2d

- Status: `done`
- Goal: A "paper at a glance" slide (or two) for Azevedo et al. (used for
  the A/B testing application, W7) — research question, why EB, main
  finding, visual.
- Inputs: [azevedo-et-al-2020-ab-testing-fat-tails.md](../references/azevedo-et-al-2020-ab-testing-fat-tails.md);
  figure to reuse: `deliverable/slides/figures/azevedo-fig1-posterior-mean.png`
  (posterior mean function, already used in W7's deep dive) — **user
  decision (2026-08-10): reuse this existing figure directly rather than
  drafting a simplified version.**
- Target files: new slide draft; eventual home in `eb-workshop.tex` overview
  mini-section.
- Definition of done: 1–2 slides — research question (how should a firm
  allocate scarce A/B-test traffic across many candidate ideas?), why EB
  (most ideas' raw estimated effects are noisy given limited sample sizes;
  need to borrow strength across ideas to decide what to ship), headline
  finding shown via the reused `azevedo-fig1-posterior-mean.png` figure
  (fat-tailed distribution of true effects / the shrinkage-at-different-
  t-stats result). — **Met, 1 frame.** "Paper at a Glance: Scaling Up A/B
  Testing" states the research question (allocating scarce experimental
  users across many ideas), the why-EB justification (raw effects too
  noisy to trust alone; posterior mean gives the ship/don't-ship rule), and
  the fat-tails finding at Bing, closing with
  `azevedo-fig1-posterior-mean.png` at `width=0.22\textwidth` (slightly
  smaller than W7's `0.25\textwidth`, to match this frame's three bullets
  vs. W7's own figure frame).
- Depends on: none (see R2a's note).
- Notes for Codex: Same third-appearance consideration as R2a/R2c — this
  image will now appear on both the overview slide and W7's deep dive,
  which is fine per the user's explicit decision; a lighter caption/less
  annotation on the overview slide can help it read as a preview rather
  than a rerun. **Followed this**: caption here is a single source line
  (no restated numbers), lighter than W7's own frame which spells out both
  worked shrinkage examples in its bullets.

### R3

- Status: `done`
- Goal: Review the Part 1 → Part 2 transition frames — specifically W9's
  sampling-model introduction and W10's normal/normal setup/derivation
  frames — and cut formulas/technical detail down to only what's load-
  bearing for what follows. This is a trim/simplify pass, not a rewrite of
  the underlying math.
- Inputs: `deliverable/slides/eb-workshop.tex` (W9 and W10 frames, currently
  ~3 + 5 frames); the W9/W10 card notes above for what each frame is
  currently carrying.
- Target files: `deliverable/slides/eb-workshop.tex`.
- Definition of done: identify, per frame in this range, what's essential
  (audience needs it to follow Part 2) vs. what's decorative/redundant
  (restates something already said, or a level of formality the talk
  doesn't need) — propose cuts to the user before editing `eb-workshop.tex`,
  since this touches the derivation the rest of Part 2 depends on. — **Met.**
  Proposed a specific 8-frame-to-5-frame plan (with the exact keep/cut list)
  via `AskUserQuestion` before touching the file; user picked the
  recommended option (merge as proposed, keep the posterior-variance
  formula as a one-line text mention rather than cutting it or keeping it
  as a display equation). Then edited `eb-workshop.tex`:
  1. **W9, 3 frames -> 2**: merged "Back to Boston Schools: The Sampling
     Model" and "The Second Level: $\theta_j \sim G$" into one "The
     Normal/Normal Model: Two Levels" frame — both defining equations kept
     ($\hat\theta_j\mid\theta_j,s_j\sim N(\theta_j,s_j^2)$ and
     $\theta_j\sim N(\mu,\tau^2)$), the redundant "two levels, one recipe"
     summary bullet cut (redundant with the untouched recipe-preview frame
     right after it). "Preview: The Three-Step EB Recipe" frame left
     unchanged.
  2. **W10, 5 frames -> 3**: merged "Setting Up the Derivation" (a near-
     verbatim formal restatement of W9's two equations), "Deriving the
     Posterior Mean: Precision-Weighting" (had an explicit Bayes'-rule
     product-of-exponentials display equation), and "Result: The Posterior
     Mean Formula" into one "Deriving the Posterior Mean" frame. Cuts: the
     Bayes'-rule density equation is now stated in words only; the
     posterior-variance formula is folded into a words-only clause rather
     than shown as its own equation/bullet. The closed-form $\theta_j^*$
     result equation itself is untouched (load-bearing for W11/W12). The
     picture frame and the plain-language recap frame were left unchanged.
  Net: 8 frames -> 5 frames, deck total 43 -> 40. Structural check: frame
  count 40/40 (`\begin{frame}`/`\end{frame}`); braces 515/515; `itemize`
  30/30 (down from 33, consistent with 3 fewer itemize-containing frames);
  display-math `\[...\]` opens/closes 7/7 (excluding `\\[0.4em]`-style
  linebreak spacing); dollar-sign count even (282); re-scanned for leaked
  `W\d+`/`R\d+` tokens in frame bodies afterward — zero hits, same script
  as R1's re-verification pass. Still no local `pdflatex`/`xelatex` in this
  environment — not compiled, structural check only.
- Depends on: none, but should probably be sequenced after R2 lands (R2
  adds new slides before this region, which may change how much scene-
  setting W9/W10 still need to do on their own). — done after R2, as
  planned; in practice R2's additions (all before "A Preview of Today's
  Examples") didn't overlap with W9/W10's content, so no further scope
  change resulted from the sequencing.
- Notes for Codex: Don't cut content that R1's or R4's changes elsewhere in
  the deck rely on referencing back to (e.g., W11 and W12 both point back at
  "the posterior mean formula from before" — confirm the trimmed version
  still supports those references before finalizing). **Followed this**:
  W11's "the posterior mean formula from before" and W12's "the shrinkage
  weight from before" both still resolve correctly to content in the
  merged "Deriving the Posterior Mean" frame — neither the $\theta_j^*$
  equation nor the $w_j$ notation was touched by the cuts.

### R4a

- Status: `done`
- Goal: Re-review the first half of Part 1 (opening/preview frames, plus
  the teacher value-added individual-estimate, distribution, and regressor-
  attenuation frames) against a "many pictures, light text, story-driven,
  example-led" style bar. Flag which frames are too text-heavy or crowded,
  and either simplify the wording or split into two frames.
- Inputs: `deliverable/slides/eb-workshop.tex` (current W1–W4 frames).
- Target files: `deliverable/slides/eb-workshop.tex`.
- Definition of done: a per-frame assessment (keep as-is / simplify text /
  split into two) presented to the user before any edits are made, then the
  approved edits applied. — **Met.** Reviewed all 9 frames across W1–W4
  (excluding R2's frames, a separate already-approved task) and presented a
  per-frame assessment in chat with a priority tag on each: 2 low priority
  (leave as-is), 1 medium (trim), 1 medium-high (trim), 3 high priority
  (add a new illustrative figure), 1 highest priority (split — the clearest
  case, since it undoes an earlier over-compression). User approved all 9
  with two tweaks (see below), then all 9 were executed:
  1. **"What Is Empirical Bayes?"** split into two frames — a text-only
     definition frame, and a new "EB Serves Three Objectives" frame that
     replaces the enumerate list with three small TikZ icons (bell curve
     for "learn the distribution," a shrink-arrow for "improve individual
     estimates" reusing W10's exact number-line motif, three ranked bars
     for "support decisions").
  2. **"A Preview of Today's Examples"** — trimmed the trailing
     explanatory clause off the four bullets R2's new "Quick Paper
     Overviews" mini-section (inserted right after this frame under task
     R2) now covers in more depth, to avoid the same four topics being
     spelled out in full twice in a row. The two bullets R2 doesn't cover
     kept their full text.
  3. **"The Problem: Noise Masquerades as Quality"** — added a new
     illustrative funnel-plot figure (school size on x, raw estimate on
     y, small/noisy schools in red scattering widely, large/precise
     schools in blue clustering near the true mean) — no bullet text cut.
  4. **"The EB Fix: Borrow Strength Across Schools"** — light trim of one
     bullet (merged two clauses into one), figure unchanged.
  5. **"How Much Does Quality Really Vary?"** — added a new illustrative
     dual-normal-curve figure (wide red curve = raw variance, narrower
     taller blue curve = true spread $G$) — no bullet text cut.
  6. **"Introducing $G$"** — the closing FE/RE-terminology caveat bullet
     (previously the densest bullet in W1–W4) trimmed from a two-clause,
     multi-line explanation down to one sentence, kept as a normal inline
     bullet (per the user's explicit tweak: no boxed aside, to avoid extra
     layout complexity).
  7. **"A Pitfall: Using $\hat\theta_j$ as a Regressor"** — added a new
     illustrative regression-lines figure (a scatter with a steep "true
     slope" line in blue and a flatter "attenuated" line in red) — no
     bullet text cut.
  8. **"The EB Fix: Regress on the Posterior Mean"** — the most crowded
     frame in W1–W4 (4 bullets, the last a long two-clause asymmetry
     argument, plus a pull-quote box) split back into two frames:
     fix+why+caveat (3 bullets), then a dedicated "Memorable Rule: Right
     Side Fixes Bias, Left Side Causes It" frame carrying the asymmetry
     argument and the existing pull-quote box — this undoes the
     2026-07-17 compression pass's merge of these same two points.
  Net: W1 2→3 frames, W4 2→3 frames (+2 total); deck 42→44 frames.
  Structural check: frame count 44/44; `tikzpicture` 8/8 (4 pre-existing +
  4 new: the icon row, funnel plot, dual-curve, regression-lines); `scope`
  3/3 (all inside the icon row); `center` 21/21; braces 618/618;
  dollar-sign count even (326); display-math `\[...\]` still 7/7 (none of
  the new content uses `\[...\]`, all figures are TikZ-only); re-scanned
  for leaked `W\d+` tokens in frame bodies — zero hits. **Not yet compiled
  in Overleaf** — this turn's 4 new TikZ figures (frame-1 icon row, funnel
  plot, dual-normal curves, regression-lines) are new since the user's
  last Overleaf confirmation (which covered R1–R3, 40 frames, plus R5's
  scatter/weight-curve figures reported separately). **Per the user's
  explicit request, execution paused here — R4b (W5–W8) will not start
  until the user has reviewed these new figures' style** (first turn this
  revision round where genuinely original illustrations, not reused paper
  figures, were added to Part 1).
- Depends on: none, but should follow R1 and R3 in execution order since
  both touch overlapping frames (R1 rewords ID leaks in this range, R3 may
  change how much the W9/W10 bridge needs W1–W4 to have already covered) —
  sequencing avoids rework, not a hard blocking dependency. — Done after
  both R1 and R3, as planned.
- Notes for Codex: This is a judgment call pass, not mechanical — present
  the assessment and get sign-off on which frames to touch before drafting
  new copy, per the "no execution without approval" rule for this revision
  round. **Followed this**: the 9-item list with per-frame current-state/
  suggestion was presented in chat (not via `AskUserQuestion`, since it
  was a multi-item list better suited to prose) and the user replied with
  blanket approval plus two specific tweaks, both applied exactly as
  specified (G's caveat trimmed inline, not boxed; execution paused before
  R4b for a figure-style review).
- **2026-08-10 sizing pass**: user confirmed in Overleaf that all 4 of
  this card's new TikZ figures (icon row, funnel plot, dual-normal curves,
  regression-lines) render correctly with no overflow, but read too small
  for back-row visibility. Enlarged the icon row 0.92->0.95\textwidth
  (frame has no competing text, so kept close to W10's already-confirmed
  0.92 ceiling); enlarged the other three (funnel plot, dual-curve,
  regression-lines) 0.42-0.44->0.5\textwidth each, and tightened the
  `\vs` immediately before each of those three figures to
  `\vspace{0.4em}` to reclaim vertical room, matching the precedent set by
  W7's 2026-07-18 sizing/spacing fix. Only `resizebox` width fractions and
  those three `\vs` swaps changed — no internal TikZ coordinates were
  touched (resizebox scales uniformly, keeping the risk reasoned-through
  rather than guessed at without a local compiler). Structural check:
  frame count unchanged (44/44, pure sizing edit); `tikzpicture` unchanged
  (8/8); braces 623/623; dollar-sign count unchanged (326); re-scanned for
  leaked `W\d+` tokens — zero hits. **Not yet re-compiled** — awaiting the
  user's next Overleaf pass to confirm the larger sizes still fit cleanly.

### R4b

- Status: `done`
- Goal: Same style re-review as R4a, applied to the second half of Part 1 —
  the many-unit-types gallery, the ranking (Kline–Rose–Walters) frames, the
  A/B testing (Azevedo) frames, and the synthesis/wrap-up frame.
- Inputs: `deliverable/slides/eb-workshop.tex` (current W5–W8 frames).
- Target files: `deliverable/slides/eb-workshop.tex`.
- Definition of done: same as R4a — per-frame assessment presented for
  approval, then approved edits applied. — **Met.** Reviewed all 8 frames
  across W5–W8, presented a per-frame issue+suggestion+priority list in
  chat (2 low priority table-anchored frames left as-is: W5's gallery
  table, W8's recurring-pattern table; 2 low-priority "optional, out of
  scope" notes on W6/W7's already-figured frames; 4 high/medium-priority
  frames flagged for a new illustrative figure). No frame needed a split
  this round (unlike R4a's one clear split case). User approved the full
  list with no scope changes, then all 4 new figures were added:
  1. **"The Design: Auditing 108 Large Employers"** (W6) — added a
     heterogeneity dot-plot: a single dot at the 2.1pp average gap with a
     red double-arrow spread bracket showing the ≈1.9pp between-firm SD,
     plus faint tick marks suggesting scattered individual firms — no
     bullet text cut.
  2. **"23 of 108 Firms"** (W6) — added an icon-array figure: 108 small
     squares in an 18×6 grid (deliberately wide/short for a low aspect
     ratio), the first 23 in red, the rest gray — a direct visual for the
     "23 of 108" statistic.
  3. **"The Setup: Screening Many Ideas With Scarce Experiments"** (W7) —
     added a decision-rule number-line figure: a shaded "don't
     ship"/"ship" split at zero with a handful of example idea-dots.
  4. **"Lean vs. Big: How Fat Tails Change the Strategy"** (W7) — added a
     two-column icon comparison: 2 large circles for "thin tails: big
     data" vs. 6 small circles for "fat tails: lean."
  All 4 new figures were deliberately designed with low height/width
  aspect ratios (~0.1–0.33) since they land on 4-bullet frames with less
  vertical headroom, and drafted directly at the eventual unified
  `0.55\textwidth` (see the sizing-pass note on R4a's card and below) with
  a `\vspace{0.4em}` before each, matching R4a's established pattern for
  bullet-heavy figure frames.
- Depends on: none, but sequence after R2b/R2c/R2d land (the new paper-
  overview slides may absorb some of what these frames currently spell out
  in text, changing what "essential" text remains here). — Done well
  after R2 (R2 landed several turns earlier); in practice none of R2's
  overview content changed what W5–W8 needed to cover, same as R3's
  sequencing turned out not to matter in practice.
- Notes for Codex: Same judgment-call caveat as R4a — get sign-off before
  drafting. **Followed this**: the 8-item list was presented in chat with
  explicit "先不要動手改，讓我看過再決定" framing honored — no edits made
  until the user replied "清單全部照做，不用調整範圍."
- **2026-08-10 unification sizing pass (same turn as R4b execution)**:
  immediately after R4b's 4 new figures were added, the user asked to
  enlarge and *unify* the sizing of all of this revision round's figures
  (R4a's 6 + R4b's 4 new ones + W6/W7's own pre-existing KRW/Azevedo
  figures = 12 total) rather than leaving them at the mismatched
  0.5/0.55/0.6/0.95 spread from the two prior sizing passes. Set
  `0.55\textwidth` uniformly across 11 of the 12: R4a's 6 (icon row down
  from 0.95; funnel/dual-curve/regression-lines up from 0.5; R5a/R5b down
  from 0.6 — note this means W1 and R5a/R5b actually got *smaller*, not
  bigger, in service of consistency, which was flagged explicitly to the
  user rather than silently applied), R4b's 4 new figures (drafted
  directly at 0.55), and W6's KRW fig6 (0.52→0.55, with fig7 kept at
  exactly half — 0.26→0.275 — to preserve the deliberate height-matching
  ratio between the two images established when they were first added).
  **One explicit exception**: W7's existing Azevedo Figure 1 was capped at
  `0.32\textwidth` rather than brought to 0.55, because that image has
  documented history (an earlier "2026-07-18 sizing/spacing fix") of
  needing a *reduction* from 0.4 down to 0.25 specifically because it
  caused a layout problem on this same 3-bullet frame — pushing to 0.55
  risked repeating that exact problem, so a smaller-but-still-improved
  0.32 was used instead and flagged to the user. R2's separate reused
  copies of the same KRW/Azevedo images (in the "Paper at a Glance"
  overview frames, at 0.42/0.21 and 0.22 respectively) were explicitly
  left untouched — the user's request named specifically "這次W6/W7兩張
  既有圖" (W6/W7's own deep-dive frames), not R2's differently-scoped
  reuse. W10's number-line (0.92) and W12's risk-curve (0.6) — both
  pre-existing, from before this revision round — were also left
  untouched. Structural check: frame count unchanged (44/44, pure content-
  within-existing-frames + sizing edit); `tikzpicture` 8→12 (4 new);
  `center` 21→25 (4 new); `\ifnum`/`\fi` 1/1 (new to this file, used by
  the icon-array figure); braces 676/676; dollar-sign count even (328);
  re-scanned for leaked `W\d+` tokens — zero hits. **Not yet re-compiled**
  — this is the third sizing pass this session and the first to touch
  W6/W7's frames; an Overleaf check is the natural next step.

### R5a

- Status: `done`
- Goal: Add a new intuitive figure to Part 2 — a scatterplot with each
  unit's raw estimate on the x-axis and its shrunk/EB posterior-mean
  estimate on the y-axis, making the "shrinkage pulls points toward the
  center, more so for noisy units" idea visible at a glance across the
  whole sample at once (complementing W10's single-unit number-line
  schematic).
- Inputs: none new — this would ideally use the same underlying data as an
  existing worked example (Boston schools VAM) if the raw values are
  recoverable from `references/`, otherwise a stylized/simulated version
  with a note that it's illustrative.
- Target files: new figure (script or TikZ) + new slide in
  `eb-workshop.tex`, most likely placed in the W10/W11 region (after the
  posterior-mean formula and EB plug-in are both established) or as part of
  R5's contribution to Part 2 generally — exact placement to be decided at
  drafting time.
- Definition of done: a scatterplot figure (points below the 45-degree line
  shrunk toward the prior mean, noisier units moving further) plus a slide
  that introduces it, with a plain-language caption. — **Met.** New frame
  "Seeing Shrinkage Across the Whole Sample" inserted right after W10's
  "What the Formula Says, in Plain Language" (see placement decision
  below). Figure is a hand-drawn TikZ scatter, not a script-generated plot:
  x-axis $\hat\theta_j$, y-axis $\theta_j^*$, a dashed 45-degree "no
  shrinkage" reference line, and 14 illustrative points in two colors —
  7 blue ("precise units," $w=0.85$, close to the diagonal) and 7 red
  ("noisy units," $w=0.35$, pulled close to $\mu$ at the origin) — reusing
  the same blue=precise/red=noisy color coding as W10's existing two-unit
  number-line picture for visual continuity. Caption explicitly states
  "Illustrative example (not real data)."
- Depends on: R3 (placement depends on what the trimmed W9/W10 region looks
  like) and ideally comes after W10/W11's existing figures so it reads as a
  complement, not a duplicate. — R3 landed first as planned; in practice
  R5a was placed right after W10 (not after W11), see the placement
  decision below.
- Notes for Codex: Clarify with the user whether this should use real data
  (if recoverable) or a clearly-labeled stylized/simulated example — don't
  fabricate numbers that look like real Boston VAM data without flagging
  them as illustrative. **Followed this**: confirmed via `AskUserQuestion`
  (2026-08-10) — no unit-level raw dataset exists anywhere in this repo
  (only PDFs/reference notes), so illustrative/stylized TikZ data was used,
  explicitly labeled in the caption, matching the deck's existing house
  style for W10/W12's hand-drawn schematics rather than inventing a new
  "looks-real" precedent.
- **2026-08-10 placement decision**: confirmed via `AskUserQuestion` —
  placed right after W10's "What the Formula Says, in Plain Language" and
  before W11's "The Empirical Step" (not after W11's own reused histogram
  figure, which was the offered alternative). Rationale: R5a illustrates
  the Bayes formula itself (known $\mu,\tau^2$), not the estimation step,
  so it belongs with W10's material; also gives a "one unit (W10's
  existing picture) -> many units at once (R5a) -> the general rule (R5b)"
  zoom-out right before the deck turns to real estimation in W11.

### R5b

- Status: `done`
- Goal: Add a new schematic figure to Part 2 illustrating the relationship
  between shrinkage magnitude and sample size (units with fewer
  observations / noisier estimates get pulled further toward the prior
  mean; units with more observations barely move) — a more general,
  population-level companion to W10's two-unit number-line picture.
- Inputs: none new — schematic/illustrative, same style as W10's and W12's
  hand-drawn TikZ figures (not a paper screenshot).
- Target files: new TikZ figure + new slide in `eb-workshop.tex`, likely
  near W10/W11 (shrinkage weight `w_j = \tau^2/(\tau^2+s_j^2)` region) —
  exact placement to be decided at drafting time.
- Definition of done: a figure showing shrinkage weight or shrinkage
  distance as a function of sample size / precision (e.g., `s_j^2`
  decreasing as `n_j` grows, and less shrinkage as a result), plus a slide
  introducing it in plain language. — **Met.** New frame "How Much
  Shrinkage? It Depends on Precision," placed immediately after R5a (a
  matched pair, per the note below). Unlike R5a, this figure needed **no**
  simulated data at all — it's a direct TikZ `plot` of the closed-form
  shrinkage weight $s_j^2/(\tau^2+s_j^2)$ (the weight placed on $\mu$,
  already derived on the "Deriving the Posterior Mean" frame two slides
  earlier) as a smooth curve over $s_j \in [0,4.3]$, rising from 0 toward
  an asymptote at 1 (marked with a dashed reference line). Two example
  points are marked on the curve ("precise unit" at small $s_j$, "noisy
  unit" at large $s_j$), reusing the same blue/red color coding as R5a and
  W10's number-line picture. Caption explicitly translates $s_j$ into
  "smaller effective sample sizes" language to satisfy the "vs. sample
  size" framing from the teacher's original request, since $s_j$ (not
  $n_j$) is what's formally in the model.
- Depends on: R3 (placement depends on the trimmed W9/W10 region) and
  R5a (should feel like a matched pair, not two unrelated figures — worth
  drafting back to back for visual consistency). — **Met**: placed
  directly adjacent to R5a (immediately following it), both inserted in
  the same edit, sharing the same color convention and figure width
  (`0.5\textwidth`/`0.48\textwidth`) for visual consistency.
- Notes for Codex: This is the "shrinkage vs. sample size" relationship
  specifically — keep it distinct from R5a's "raw vs. shrunk scatterplot,"
  which is about the *estimates*, not the *sample-size driver* of
  shrinkage. **Followed this**: R5b's x-axis is $s_j$ specifically (not
  $\hat\theta_j$), and its y-axis is the shrinkage weight itself, not an
  estimate value — no overlap in what each figure actually plots.
- **2026-08-10 sizing pass**: user confirmed in Overleaf that both R5a's
  and R5b's figures render correctly with no overflow, but read too small.
  Enlarged both from `0.5\textwidth`/`0.48\textwidth` to
  `0.6\textwidth` each, matching W12's already-confirmed 0.6\textwidth
  ceiling for a similarly light (single-intro-line-then-figure) frame
  layout — no `\vs` tightening needed here since these two frames have
  much less competing text than the W1-W4 figures sized in the same pass
  (see R4a's card note). No internal TikZ coordinates touched. Structural
  check: frame count unchanged (44/44); `tikzpicture` unchanged (8/8);
  braces 623/623; re-scanned for leaked `W\d+` tokens — zero hits. **Not
  yet re-compiled** — awaiting the user's next Overleaf pass.

### R6

- Status: `done`
- Goal: The user's local compile check (Overleaf) found that 5 specific
  frames had *genuine* content overflow — real bullet/figure/caption content
  cut off below the nav bar, not just visual crowding — left over from the
  three prior sizing passes (R4a/R4b/R5b's `0.55\textwidth` unification).
  Fix all 5 without changing any bullet wording or figure meaning, using this
  priority order: (a) shrink figure width/proportions first, (b) tighten
  vertical spacing between bullets and figures, (c) trim a line only if a
  single overly-long line is the direct cause, (d) split into two frames only
  as a last resort.
- Inputs: none new — pure layout fix using the existing figures/bullets
  already in `eb-workshop.tex`.
- Target files: `deliverable/slides/eb-workshop.tex` (5 frames only — "The
  Problem: Noise Masquerades as Quality," "A Pitfall: Using $\hat\theta_j$ as
  a Regressor," "A Gallery of Many-Unit Settings," "23 of 108 Firms," "The
  Fat-Tail Finding at Bing"). No other frame touched.
- Definition of done: all 5 frames' full content (every bullet, the complete
  figure, and the complete caption) renders above the nav bar with a local
  `pdflatex` compile, verified both by the compiler's own overfull-box
  warnings and by visually inspecting rendered page images. — **Met.** Local
  `pdflatex` (MiKTeX) was available in this environment, so this was a real
  compile-and-inspect loop, not a structural-only check like every prior
  round. Before touching any of the 5 target frames, an unrelated problem was
  found and fixed first: line 199 (the "A Preview of Today's Examples" frame
  title) had a large block of chat-instruction text pasted into the middle of
  it, splitting the title into "A Previ" + the pasted block + "ew of Today's
  Examples" — this would have broken the entire compile. Flagged to the user
  and repaired by restoring the plain `\begin{frame}{A Preview of Today's
  Examples}` title; confirmed via `grep` that no other spot in the file had
  the same corruption.
  With that fixed, an initial compile located the 5 real overflow frames by
  their `Overfull \vbox ... too high` warnings (ranging from ~10pt to
  ~133pt), then each was iteratively edited and re-compiled until its
  warning cleared:
  1. **"The Problem: Noise Masquerades as Quality"** (funnel-plot figure,
     ~133pt overflow — the worst of the 5): the TikZ picture's y-axis was
     disproportionately tall for its width (aspect ≈0.9). Flattened it by
     scaling every y-coordinate (axis extent, funnel-curve amplitude, all 11
     data points, both labels) down by a combined ~0.39x, and reduced
     `\resizebox` from `0.55\textwidth` to `0.38\textwidth`. No bullet text
     touched; the funnel shape and small/large-school contrast are
     unchanged, just flatter.
  2. **"A Pitfall: Using $\hat\theta_j$ as a Regressor"** (regression-lines
     figure, x-axis fully cut off, ~65pt overflow): same fix — flattened the
     y-axis (scaled y-coordinates down ~0.6x), reduced `\resizebox` from
     `0.55\textwidth` to `0.38\textwidth`, tightened the pre-figure
     `\vspace` from `0.4em` to `0.05em`. Both regression lines and all 5
     scatter points keep their original relative positions, just compressed
     vertically.
  3. **"A Gallery of Many-Unit Settings"** (table, worst-affected — the
     Police/Gonçalves-Mello row was fully missing and the Doctors/Hospitals
     row was cut, ~93pt vbox + ~14pt hbox overflow): switched the table font
     from `\footnotesize` to `\scriptsize`, set `\arraystretch` to `0.6` (was
     effectively `1.0`), removed the `[0.4em]` extra inter-row padding after
     each of the first three rows, tightened the column widths slightly
     (first column changed from an unconstrained `l` to a fixed `p{1.6cm}`,
     third column `5.4cm` narrowed from the original de-facto width) to also
     clear a horizontal overfull-hbox warning, and tightened the `\vs`
     (1em) before/after the table down to `\vspace{0.02em}`. All 4 rows'
     text is completely unchanged — same institutions, same citations, same
     findings.
  4. **"23 of 108 Firms: Naming Names with Statistical Confidence"** (icon
     array, bottom rows + full caption cut, ~34pt overflow): the grid was
     6 rows × 18 columns (aspect ≈0.33); reshaped to 4 rows × 27 columns
     (same 108 total squares, same 23 flagged in red), which flattens the
     aspect to ≈0.15. Also reduced `\resizebox` from `0.55\textwidth` to
     `0.5\textwidth` and tightened the pre-figure `\vspace` from `0.4em` to
     `0.2em`. The 23-red-of-108 count and meaning are unchanged — only the
     grid's row/column shape changed.
  5. **"The Fat-Tail Finding at Bing"** (posterior-mean-vs-signal image,
     mildest — final caption line touching the nav bar, ~10pt overflow):
     reduced `\includegraphics` from `0.32\textwidth` to `0.27\textwidth`
     and tightened the pre-image `\vspace` from `0.3em` to `0.1em`. Image
     and caption text unchanged.
  Final verification: recompiled the whole 44-frame deck with `pdflatex`
  (MiKTeX) after all 5 fixes. The `Overfull \vbox`/`\hbox` warnings that had
  been anchored inside these 5 frames' line ranges are gone; the deck's
  pre-existing overfull warnings on *other*, out-of-scope frames (the R2
  "Paper at a Glance: Teacher & School Value-Added" frame, W3's "How Much
  Does Quality Really Vary?", W6's "The Design: Auditing 108 Large
  Employers," W7's "Lean vs. Big," the W8 recap table, R5a's "Seeing
  Shrinkage Across the Whole Sample," and W12's "Picture: One Unit's Risk"
  frame — none named in this task) are untouched and left exactly as they
  were, per the instruction not to touch any frame outside the named 5.
  Additionally rendered the 5 target frames to PNG (`pdftoppm`, pages 12,
  16, 19, 22, 24) and visually confirmed every bullet, the complete
  figure/grid/table, and the complete caption sit above the nav bar with a
  visible safety margin on each. Re-scanned the 5 edited frames' visible
  text for any new `W\d+`/`R\d+`-style leaks — none introduced (only TikZ
  coordinates, `\resizebox`/`\includegraphics` widths, `\vspace` amounts,
  and table formatting commands were changed).
- Depends on: R4a, R4b, R5b (all three sizing passes that produced the
  `0.55\textwidth`-era layout this task was verifying). — all done before
  this task started.
- Notes for Codex: This was the first task in the whole R1–R5(+R6) round
  with a local `pdflatex` available (MiKTeX, confirmed via `pdflatex
  --version` before starting) — every prior round's "structural check only"
  disclaimers no longer apply to this task's own verification, though they
  remain accurate historical statements about *those* tasks. The deck has a
  long-standing, unrelated `! Undefined control sequence` /
  `Missing \begin{document}` pair at line 23 (`\setitemize`, likely an
  `enumitem`-family command used without its package) that appears on every
  compile, before and after this task's edits, and does not stop `pdflatex`
  from producing all 44 pages in nonstopmode (`pdflatex`'s recovery mode
  just skips the malformed setting and continues) — left untouched as
  out-of-scope for this task, flagged here in case a future task wants a
  fully warning-clean compile.

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
