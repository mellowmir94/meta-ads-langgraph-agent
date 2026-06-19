# Module 0 - Python Setup

## Goal

Prepare a clean Python development environment for the Meta Ads LangGraph Agent.

This module is not about building agent logic yet. It is about making sure the local setup is reliable before adding LangChain, LangGraph, tools, RAG, memory, and observability.

## Recommended Stack

- Python 3.11 or 3.12 for stable AI package compatibility
- `venv` for local dependency isolation
- `pip` for package installation
- `pytest` for tests
- `ruff` for linting
- Git + GitHub for portfolio history

The current local environment works with Python 3.14.3, but for long-term LangChain and LangGraph work, Python 3.11 or 3.12 is the safer default.

## Why This Exists

Production AI projects depend on repeatable environments.

Without a clean setup, errors become hard to diagnose:

- package version conflicts
- missing API keys
- scripts running against the wrong Python interpreter
- inconsistent test results
- GitHub repos that are hard for recruiters or engineers to run

This module creates a baseline that future modules can build on.

## Setup Commands

From the project root:

```bash
cd C:\Users\AmirKhalil\Documents\CC\meta-ads-langgraph-agent
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it in PowerShell:

```bash
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Run tests:

```bash
python -m pytest
```

Run lint:

```bash
python -m ruff check .
```

## Environment Variables

Create a local `.env` file:

```bash
Copy-Item .env.example .env
```

Use OpenAI:

```env
LLM_PROVIDER=openai
OPENAI_API_KEY=your_key_here
LLM_MODEL=gpt-4o-mini
```

Or use Claude:

```env
LLM_PROVIDER=anthropic
ANTHROPIC_API_KEY=your_key_here
LLM_MODEL=claude-3-5-haiku-latest
```

Never commit `.env`.

## Run The Phase 1 Chat

```bash
python -m app.chat
```

This validates:

- Python imports work
- `.env` loading works
- settings validation works
- logging is configured
- the selected LLM provider can be called

## Checkpoint

Module 0 is complete when:

- virtual environment exists
- dependencies install successfully
- `python -m pytest` passes
- `python -m ruff check .` passes
- `.env` exists locally but is not committed
- GitHub remote is connected
- `main` is pushed to GitHub

## GitHub Commit

Suggested commit message:

```text
docs: add module 0 python setup guide
```

## Next Module

After this, move into Phase 2 foundations:

- install LangChain packages
- refactor direct LLM calls into LangChain chat models
- introduce prompt templates
- introduce structured outputs
