from __future__ import annotations

from dotenv import load_dotenv
from langsmith import evaluate

from app.chat import run_chat_turn
from app.config import Settings
from evaluations.dataset import LANGSMITH_DATASET_NAME
from evaluations.evaluators import metric_accuracy, read_only_safety, recommendation_structure


def target(inputs: dict) -> dict[str, str]:
    settings = Settings.from_env()
    response = run_chat_turn(
        user_input=str(inputs["input_text"]),
        llm_provider=settings.llm_provider,
        llm_model=settings.llm_model,
        llm_temperature=settings.llm_temperature,
    )
    return {"response": response}


def main() -> None:
    load_dotenv(".env")
    evaluate(
        target,
        data=LANGSMITH_DATASET_NAME,
        evaluators=[metric_accuracy, recommendation_structure, read_only_safety],
        experiment_prefix="meta-ads-agent",
        description="Module 2 experiment: metric accuracy, structure, and read-only safety.",
        max_concurrency=1,
    )


if __name__ == "__main__":
    main()
