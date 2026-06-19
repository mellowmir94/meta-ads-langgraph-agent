# Module 1 - Observability

## Goal

Add basic LangSmith tracing so each chat turn can be inspected after it runs.

Observability answers:

- What input did the app receive?
- What model was called?
- What output came back?
- Did the call fail?
- How long did it take?

## Why This Exists

LLM apps are difficult to debug from terminal output alone. A trace gives a record of the request lifecycle, which becomes more important when the project later adds LangChain chains, tools, RAG, agents, and LangGraph workflows.

## Local Setup

Add these to local `.env`:

```env
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=your_langsmith_key_here
LANGSMITH_PROJECT=meta-ads-langgraph-agent
```

Never commit `.env`.

## Run A Trace

```bash
python -m app.chat
```

Prompt:

```text
Review this campaign: spend RM100, leads 5, clicks 80, impressions 4000.
```

## Verify In LangSmith

1. Open LangSmith.
2. Go to the `meta-ads-langgraph-agent` project.
3. Open the latest trace.
4. Confirm the `chat_turn` run appears.
5. Inspect inputs, outputs, timing, and any errors.

## Portfolio Value

This shows recruiters that the project is not only calling an LLM, but also instrumented for debugging and production-style inspection.

## GitHub Commit

Suggested commit message:

```text
feat: add langsmith tracing for chat turns
```
