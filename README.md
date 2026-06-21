# Meta Ads LangGraph Agent

AI-powered Meta Ads monitoring agent built as a production-quality AI engineering portfolio project.

This project starts simple and evolves through LLM fundamentals, LangChain, tools, RAG, agents, LangGraph workflows, persistence, Telegram automation, LangSmith observability, and production readiness.

## Phase 1 Scope

Current milestone: **LLM Fundamentals**

Implemented:

- Python project structure
- environment variable configuration
- Gemini, OpenAI, or Claude chat client wrapper
- simple terminal chat interface
- structured logging setup
- first tests
- architecture documentation

Not implemented yet:

- LangChain abstractions
- Meta Ads CSV tools
- RAG knowledge base
- LangGraph workflow
- persistence
- Telegram notifications

## Architecture

```text
User
  |
  v
Terminal Chat Interface
  |
  v
Settings + Logging
  |
  v
LLM Client Wrapper
  |
  +--> OpenAI
  |
  +--> Anthropic Claude
  |
  +--> Google Gemini
```

The initial architecture is intentionally small. The goal is to learn the LLM boundary first before adding LangChain and LangGraph abstractions.

## Project Structure

```text
meta-ads-langgraph-agent/
├── app/
├── agents/
├── tools/
├── workflows/
├── database/
├── data/
├── tests/
├── docs/
├── notebooks/
├── README.md
├── requirements.txt
├── pyproject.toml
├── .env.example
```

## Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create local environment variables:

```bash
Copy-Item .env.example .env
```

For free-only learning, use a Google AI Studio free-tier key and set `GEMINI_API_KEY`.
Do not enable billing unless you intentionally want paid API usage.

## Run Chat

Gemini free-tier learning setup:

```bash
$env:LLM_PROVIDER="gemini"
$env:LLM_MODEL="gemini-3.1-flash-lite"
python -m app.chat
```

OpenAI:

```bash
$env:LLM_PROVIDER="openai"
$env:LLM_MODEL="gpt-4o-mini"
python -m app.chat
```

Claude:

```bash
$env:LLM_PROVIDER="anthropic"
$env:LLM_MODEL="claude-3-5-haiku-latest"
python -m app.chat
```

## Run Tests

```bash
pytest
```

## Run Evaluation

```bash
python -m evaluations.run_code_eval
```

Optional LangSmith dataset and experiment:

```bash
python -m evaluations.sync_langsmith_dataset
python -m evaluations.run_langsmith_experiment
```

## Run Production Check

```bash
python -m workflows.production_check
```

## Safety Rules

This agent is read-only. It must never modify campaigns, budgets, ads, ad sets, or creatives automatically. Any future write action must require explicit human approval.

## Cost Safety

The recommended learning setup uses `LLM_PROVIDER=gemini` and `LLM_MODEL=gemini-3.1-flash-lite` with a free-tier Google AI Studio key.

Keep billing disabled if you want free-only usage. Free tier limits can change, so monitor usage in Google AI Studio.

## Observability

LangSmith tracing is optional in Phase 1 and becomes useful when LangChain and LangGraph are introduced.

Local `.env` placeholders:

```env
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=your_langsmith_key_here
LANGSMITH_PROJECT=meta-ads-langgraph-agent
```

When tracing is enabled, each terminal chat request is recorded as a `chat_turn` run in LangSmith.

Recommendations must include:

- problem
- evidence
- impact
- recommended action

## Roadmap

1. Phase 1 - LLM Fundamentals
2. Phase 2 - LangChain Fundamentals
3. Phase 3 - Tools
4. Phase 4 - RAG
5. Phase 5 - Agent
6. Phase 6 - LangGraph
7. Phase 7 - Persistence
8. Phase 8 - Telegram
9. Phase 9 - LangSmith
10. Phase 10 - Production Readiness

## Learning Guides

- [Module 0 - Python Setup](docs/module-0-python-setup.md)
- [Module 1 - Observability](docs/module-1-observability.md)
- [Module 2 - Evaluation](docs/module-2-evaluation.md)
- [Module 3 - Moving Towards Production](docs/module-3-production.md)
- [Phase 1 Architecture](docs/phase-1-architecture.md)
