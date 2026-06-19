# Meta Ads LangGraph Agent

AI-powered Meta Ads monitoring agent built as a production-quality AI engineering portfolio project.

This project starts simple and evolves through LLM fundamentals, LangChain, tools, RAG, agents, LangGraph workflows, persistence, Telegram automation, LangSmith observability, and production readiness.

## Phase 1 Scope

Current milestone: **LLM Fundamentals**

Implemented:

- Python project structure
- environment variable configuration
- OpenAI or Claude chat client wrapper
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

Then set either `OPENAI_API_KEY` or `ANTHROPIC_API_KEY`.

## Run Chat

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

Gemini:

```bash
$env:LLM_PROVIDER="gemini"
$env:LLM_MODEL="gemini-3.5-flash"
python -m app.chat
```

## Run Tests

```bash
pytest
```

## Safety Rules

This agent is read-only. It must never modify campaigns, budgets, ads, ad sets, or creatives automatically. Any future write action must require explicit human approval.

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
- [Phase 1 Architecture](docs/phase-1-architecture.md)
