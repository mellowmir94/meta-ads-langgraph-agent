from __future__ import annotations

import logging

from dotenv import load_dotenv

from app.config import Settings
from app.llm_client import create_llm_client
from app.logging_config import configure_logging

LOGGER = logging.getLogger(__name__)

SYSTEM_PROMPT = """
You are a read-only Meta Ads monitoring assistant for local service businesses.
You help explain campaign performance, risks, and optimization ideas.
Never claim that you changed, paused, deleted, created, or edited any campaign asset.
Recommendations must include problem, evidence, impact, and recommended action.
""".strip()


def build_user_prompt(user_input: str) -> str:
    return user_input.strip()


def run_chat() -> None:
    load_dotenv()
    settings = Settings.from_env()
    configure_logging(settings.log_level)

    client = create_llm_client(settings)

    LOGGER.info(
        "Starting chat with provider=%s model=%s",
        settings.llm_provider,
        settings.llm_model,
    )
    print("Meta Ads AI Agent chat. Type 'exit' or 'quit' to stop.")

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            print("Bye.")
            return

        if not user_input:
            continue

        response = client.chat(
            system_prompt=SYSTEM_PROMPT,
            user_prompt=build_user_prompt(user_input),
        )
        print(f"\nAgent: {response}")


if __name__ == "__main__":
    run_chat()
