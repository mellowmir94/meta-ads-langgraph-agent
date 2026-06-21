# Module 2 - Evaluation

## Goal

Build a repeatable way to test whether the agent gives correct, safe, and useful Meta Ads recommendations.

## Architecture

```text
Evaluation Dataset
  -> Code-Based Metric Evaluator
  -> Safety and Structure Rubric
  -> Test Suite / CLI Report
```

## Why This Exists

LLM responses can sound confident while still being wrong. Evaluation gives the project a quality gate before prompts, tools, RAG, agents, and LangGraph workflows become more complex.

For this project, evaluation starts with deterministic checks:

- CTR calculation
- CPC calculation
- CPM calculation
- CPL calculation
- conversion rate calculation
- required recommendation fields
- read-only safety

## Dataset

Current dataset:

```text
data/evaluation/meta_ads_eval_cases.json
```

Each case includes:

- input prompt
- campaign metrics
- expected calculated metrics
- expected high-level decision label

## Run Code-Based Evaluation

```bash
python -m evaluations.run_code_eval
```

Expected result:

```text
Code eval results: 3/3 passed
PASS baseline_lead_gen
PASS no_leads_wasted_spend
PASS low_ctr_high_cpc
```

## Sync LangSmith Dataset

```bash
python -m evaluations.sync_langsmith_dataset
```

This creates or updates:

```text
meta-ads-monitoring-eval-v1
```

## Run LangSmith Experiment

This runs the current chat agent against the dataset and scores each output with deterministic evaluators:

```bash
python -m evaluations.run_langsmith_experiment
```

Evaluators:

- `metric_accuracy`
- `recommendation_structure`
- `read_only_safety`

This uses live LLM calls. For free-only learning, keep the dataset small and use `gemini-3.1-flash-lite`.

## LLM-as-Judge

The project includes an LLM judge prompt in:

```text
evaluations/llm_judge.py
```

Use it later when deterministic checks are not enough, for example judging whether a recommendation is practical for a local service business.

## Pairwise Evaluation

The project includes a pairwise comparison helper in:

```text
evaluations/pairwise.py
```

Use it later to compare two prompt versions or two model versions.

## Run Tests

```bash
pytest
```

## What This Demonstrates

This gives the portfolio project a basic evaluation harness. Recruiters and engineers can see that the agent is not only generating text; the project has objective checks for correctness and safety.

## Next Steps

Later Module 2 lessons will add:

- larger LangSmith datasets
- richer experiment metadata
- stronger LLM-as-judge criteria
- pairwise comparison between prompt versions

## GitHub Commit

Suggested commit message:

```text
feat: add code-based evaluation dataset
```
