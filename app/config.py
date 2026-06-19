from __future__ import annotations

import os
from collections.abc import Mapping
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    llm_provider: str
    llm_model: str
    llm_temperature: float
    log_level: str
    openai_api_key: str | None
    anthropic_api_key: str | None
    gemini_api_key: str | None

    @classmethod
    def from_env(cls, env: Mapping[str, str] | None = None) -> Settings:
        source = env or os.environ
        provider = source.get("LLM_PROVIDER", "openai").strip().lower()

        if provider not in {"openai", "anthropic", "gemini"}:
            raise ValueError("LLM_PROVIDER must be 'openai', 'anthropic', or 'gemini'.")

        default_models = {
            "openai": "gpt-4o-mini",
            "anthropic": "claude-3-5-haiku-latest",
            "gemini": "gemini-3.1-flash-lite",
        }

        return cls(
            llm_provider=provider,
            llm_model=source.get("LLM_MODEL", default_models[provider]).strip(),
            llm_temperature=float(source.get("LLM_TEMPERATURE", "0.2")),
            log_level=source.get("LOG_LEVEL", "INFO").strip().upper(),
            openai_api_key=source.get("OPENAI_API_KEY") or None,
            anthropic_api_key=source.get("ANTHROPIC_API_KEY") or None,
            gemini_api_key=source.get("GEMINI_API_KEY") or source.get("GOOGLE_API_KEY") or None,
        )

    def api_key_for_provider(self) -> str:
        if self.llm_provider == "openai" and self.openai_api_key:
            return self.openai_api_key
        if self.llm_provider == "anthropic" and self.anthropic_api_key:
            return self.anthropic_api_key
        if self.llm_provider == "gemini" and self.gemini_api_key:
            return self.gemini_api_key
        raise ValueError(f"Missing API key for provider '{self.llm_provider}'.")
