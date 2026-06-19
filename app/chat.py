from __future__ import annotations

import logging

from dotenv import load_dotenv
from langsmith import traceable

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


def format_chat_error(error: Exception) -> str:
    message = str(error)
    if "503" in message and "UNAVAILABLE" in message:
        return (
            "The LLM provider is temporarily unavailable because of high demand. "
            "Try again in a moment or switch to a lighter model."
        )

    return "The LLM request failed. Check your provider settings and try again."


@traceable(name="chat_turn", run_type="chain")
def run_chat_turn(user_input: str, settings: Settings) -> str:
    client = create_llm_client(settings)
    return client.chat(
        system_prompt=SYSTEM_PROMPT,
        user_prompt=build_user_prompt(user_input),
    )


def run_chat() -> None:
    load_dotenv()
    settings = Settings.from_env()
    configure_logging(settings.log_level)

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

        try:
            response = run_chat_turn(
                user_input=user_input,
                settings=settings,
            )
        except Exception as error:
            LOGGER.exception("Chat request failed")
            print(f"\nAgent: {format_chat_error(error)}")
            continue

        print(f"\nAgent: {response}")


if __name__ == "__main__":
    run_chat()
