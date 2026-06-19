# Phase 1 Architecture

## What We Are Building

Phase 1 creates the smallest useful version of the project:

- a Python application package
- environment-based configuration
- logging
- an LLM client wrapper
- a terminal chat interface
- tests for configuration and prompt handling

## Why This Exists

Before adding LangChain or LangGraph, the project needs a clear boundary between application code and the LLM provider.

That boundary matters because later phases will replace direct chat calls with:

- LangChain prompt templates
- structured output parsers
- tools
- retrieval
- agent loops
- LangGraph state transitions

Starting with a small wrapper makes the later refactors easy to understand.

## Current Runtime Flow

```text
python -m app.chat
  -> load .env
  -> validate settings
  -> configure logging
  -> create provider-specific LLM client
  -> run terminal chat loop
```

## Safety Position

The project is read-only. The assistant can explain and recommend, but it must not perform any Meta Ads write action.

The system prompt enforces the initial safety policy:

- no campaign edits
- no budget edits
- no ad creation
- no ad deletion
- recommendations must include problem, evidence, impact, and recommended action

These safety rules will become stronger later through tests, structured outputs, and approval gates.

## Next Phase

Phase 2 will refactor the direct LLM call into LangChain concepts:

- chat model abstraction
- prompt templates
- output parsers
- structured response schemas
