---
name: simulation-runner
description: Use when the user wants help designing, running, inspecting, or summarizing a simulation, numerical experiment, or computational exercise, including setting up code, choosing parameters, and interpreting outputs.
---

# Simulation Runner

Use this skill when the user is doing simulation-based research or wants help with a numerical experiment.

Design the experiment around the research claim its output will support. A quick exploratory run only needs enough structure to answer the immediate question.

## What to inspect

Inspect only the files needed for the task:

- existing simulation results or related files in `finding/`
- simulation templates in `templates/finding/`
- the most relevant theory note or draft in `deliverable/paper/`

Treat the most relevant LaTeX file in `deliverable/paper/` as a high-value source of project context because it often records the latest version of the theory, motivation, and notation.

## Output targets

Default output is one or more of the following, depending on the user's request:

- an R simulation script or R Markdown notebook in `finding/`
- a plain-language explanation of what the simulation design is testing

## Workflow

When helping with a simulation:

1. clarify the research question or theoretical mechanism being tested
2. identify the minimum simulation design needed to answer that question
3. default to R unless the user asks for another language or the existing project clearly uses something else
4. start from the R Markdown simulation template in `templates/finding/template-simulation.Rmd` when it is a good fit
5. make assumptions and parameter choices explicit, using the checks below for a run that will support a research claim
6. implement or revise the simulation code
7. inspect outputs and identify the main patterns
8. summarize what the simulation suggests and what it cannot establish

## A simulation that will support a research claim

**Before running it**, write the sentence the proposed table should let the reader assess. In the existing script, notebook or change, identify the estimand of each estimator, obtain its true target from the data-generating process (DGP), and give the sampling and replication design. State which relevant assumptions hold by construction or can be checked. Label deliberate violations and say which target remains meaningful there. For example, a fixed-order pilot can check the finite-sample interval under that design. A claim about an increasing order needs an explicit sequence of orders. Choose the replication budget with the precision needed for the comparison in mind.

**When reporting it**, retain the rerun command, input and code versions, random seed (and stream scheme for parallel draws), and per-replication results or sufficient diagnostics in the project's existing outputs. Give attempted, successful and failed replication counts by design and method, with the denominator and failure treatment used for each metric. Coverage compares the interval with the DGP target. If coverage is conditional on a successful fit, say so and report the failure rate alongside it.

Report Monte Carlo uncertainty for the headline metric. For independent replications with coverage proportion `p` over `m` valid intervals, its estimated MC standard error is `sqrt(p * (1 - p) / m)`. Methods evaluated on the same simulated samples have paired results. For a difference in coverage, use the standard error of the replication-level indicator differences on a stated common set of draws. Keep Monte Carlo uncertainty separate from the estimator's sampling standard error. [Monte Carlo design and reporting](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/rules/simulation-conventions.md)

## Writing and coding rules

- Keep the code readable and reproducible.
- Default to R for simulation work unless the user requests another language or the project already has a different established language.
- Prefer `templates/finding/template-simulation.Rmd` as the starting point when creating a new simulation notebook.
- Make parameter choices explicit rather than implicit.
- Distinguish clearly between numerical evidence and formal proof.
- Prefer the simplest simulation design that answers the research question.
- When the simulation has limitations, state them clearly.
- When useful, suggest robustness checks or alternative parameter settings.

## Good output standard

A good simulation workflow should let a future reader quickly answer:

- What is the simulation testing?
- What assumptions and parameters were used?
- What outputs matter?
- What do the results suggest?
- What limitations remain?

Default to medium detail: enough detail to reproduce and interpret the exercise without turning the note or summary into a code dump.

## Example prompt patterns

Use this skill when the user asks things like:

- help me design a simulation for this model
- write a simulation script for this mechanism
- inspect these simulation results
- summarize what this numerical exercise shows
- suggest robustness checks for this simulation
- connect this simulation to my theory notes
