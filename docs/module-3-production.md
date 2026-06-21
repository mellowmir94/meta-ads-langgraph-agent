# Module 3 - Moving Towards Production

## Goal

Move the project from a working prototype toward a repeatable production-style workflow.

## Architecture

```text
Code Eval
  -> Online Eval Scoring
  -> Insights Agent
  -> Production Check CLI
  -> CI Automation
```

## What Was Added

- Insights agent for summarizing production readiness signals
- Online eval scoring for real responses
- Production check CLI
- GitHub Actions CI workflow

## Run Production Check

```bash
python -m workflows.production_check
```

Expected output:

```text
Production status: ready
Summary: Code eval passed 3/3 case(s). Online eval reviewed 0 run(s).
Risks:
- none
Next actions:
- Proceed to the next implementation milestone.
```

## Run Full Local Validation

```bash
python -m ruff check .
python -m pytest
python -m evaluations.run_code_eval
python -m workflows.production_check
```

## Why This Matters

Production AI work is not only model calls. A credible system needs repeatable checks, evaluation gates, monitoring signals, and automation. This module adds those foundations without introducing unnecessary infrastructure.

## Next Milestone

The next real implementation milestone is LangChain fundamentals:

- chat model abstraction
- prompt templates
- structured outputs
- improved evaluation targets
