from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from app.config import Settings


class ChatClient(Protocol):
    def chat(self, system_prompt: str, user_prompt: str) -> str:
        """Return one assistant response for a single user message."""


@dataclass(frozen=True)
class OpenAIChatClient:
    api_key: str
    model: str
    temperature: float

    def chat(self, system_prompt: str, user_prompt: str) -> str:
        from openai import OpenAI

        client = OpenAI(api_key=self.api_key)
        response = client.chat.completions.create(
            model=self.model,
            temperature=self.temperature,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )

        content = response.choices[0].message.content
        return content or ""


@dataclass(frozen=True)
class AnthropicChatClient:
    api_key: str
    model: str
    temperature: float

    def chat(self, system_prompt: str, user_prompt: str) -> str:
        from anthropic import Anthropic

        client = Anthropic(api_key=self.api_key)
        response = client.messages.create(
            model=self.model,
            system=system_prompt,
            max_tokens=1000,
            temperature=self.temperature,
            messages=[{"role": "user", "content": user_prompt}],
        )

        return "".join(block.text for block in response.content if block.type == "text")


@dataclass(frozen=True)
class GeminiChatClient:
    api_key: str
    model: str
    temperature: float

    def chat(self, system_prompt: str, user_prompt: str) -> str:
        from google import genai
        from google.genai import types

        client = genai.Client(api_key=self.api_key)
        response = client.models.generate_content(
            model=self.model,
            contents=user_prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=self.temperature,
            ),
        )

        return response.text or ""


def create_llm_client(settings: Settings) -> ChatClient:
    api_key = settings.api_key_for_provider()

    if settings.llm_provider == "openai":
        return OpenAIChatClient(
            api_key=api_key,
            model=settings.llm_model,
            temperature=settings.llm_temperature,
        )

    if settings.llm_provider == "anthropic":
        return AnthropicChatClient(
            api_key=api_key,
            model=settings.llm_model,
            temperature=settings.llm_temperature,
        )

    if settings.llm_provider == "gemini":
        return GeminiChatClient(
            api_key=api_key,
            model=settings.llm_model,
            temperature=settings.llm_temperature,
        )

    raise ValueError(f"Unsupported LLM provider: {settings.llm_provider}")
