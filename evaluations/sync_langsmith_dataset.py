from __future__ import annotations

from dotenv import load_dotenv
from langsmith import Client

from evaluations.dataset import LANGSMITH_DATASET_NAME, load_evaluation_cases


def sync_dataset() -> None:
    load_dotenv(".env")
    client = Client()
    dataset = _get_or_create_dataset(client)
    existing_case_ids = {
        example.metadata.get("case_id")
        for example in client.list_examples(dataset_id=dataset.id)
        if example.metadata
    }

    created = 0
    for case in load_evaluation_cases():
        if case.case_id in existing_case_ids:
            continue

        client.create_example(
            dataset_id=dataset.id,
            inputs=case.to_langsmith_inputs(),
            outputs=case.to_langsmith_outputs(),
            metadata={"case_id": case.case_id},
        )
        created += 1

    print(f"LangSmith dataset: {LANGSMITH_DATASET_NAME}")
    print(f"Created examples: {created}")


def _get_or_create_dataset(client: Client):
    try:
        return client.read_dataset(dataset_name=LANGSMITH_DATASET_NAME)
    except Exception:
        return client.create_dataset(
            dataset_name=LANGSMITH_DATASET_NAME,
            description="Meta Ads monitoring evaluation cases for metrics and recommendations.",
        )


if __name__ == "__main__":
    sync_dataset()
