import pytest

from app.config import Settings


def test_settings_defaults_to_openai() -> None:
    settings = Settings.from_env({})

    assert settings.llm_provider == "openai"
    assert settings.llm_model == "gpt-4o-mini"
    assert settings.llm_temperature == 0.2
    assert settings.log_level == "INFO"


def test_settings_supports_anthropic_defaults() -> None:
    settings = Settings.from_env({"LLM_PROVIDER": "anthropic"})

    assert settings.llm_provider == "anthropic"
    assert settings.llm_model == "claude-3-5-haiku-latest"


def test_settings_supports_gemini_defaults() -> None:
    settings = Settings.from_env({"LLM_PROVIDER": "gemini"})

    assert settings.llm_provider == "gemini"
    assert settings.llm_model == "gemini-3.1-flash-lite"


def test_settings_rejects_unknown_provider() -> None:
    with pytest.raises(ValueError, match="LLM_PROVIDER"):
        Settings.from_env({"LLM_PROVIDER": "local"})


def test_api_key_for_selected_provider() -> None:
    settings = Settings.from_env({"LLM_PROVIDER": "openai", "OPENAI_API_KEY": "test-key"})

    assert settings.api_key_for_provider() == "test-key"


def test_api_key_missing_for_selected_provider() -> None:
    settings = Settings.from_env({"LLM_PROVIDER": "anthropic"})

    with pytest.raises(ValueError, match="Missing API key"):
        settings.api_key_for_provider()


def test_api_key_supports_gemini_key() -> None:
    settings = Settings.from_env({"LLM_PROVIDER": "gemini", "GEMINI_API_KEY": "test-key"})

    assert settings.api_key_for_provider() == "test-key"


def test_api_key_supports_google_key_alias_for_gemini() -> None:
    settings = Settings.from_env({"LLM_PROVIDER": "gemini", "GOOGLE_API_KEY": "test-key"})

    assert settings.api_key_for_provider() == "test-key"
