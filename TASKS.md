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
