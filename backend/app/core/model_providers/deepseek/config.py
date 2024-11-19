from langchain_openai import ChatOpenAI
from crewai import LLM

from app.models import ModelCategory

PROVIDER_CONFIG = {
    "provider_name": "deepseek",
    "base_url": "https://api.deepseek.com",
    "api_key": "sk-558a1f1b9957484eb52de0ddc2f9524a",
    "icon": "openai_icon",
    "description": "Deepseek OpenAI API provider",
}

SUPPORTED_MODELS = [
    {
        "name": "deepseek-chat",
        "categories": [ModelCategory.LLM, ModelCategory.CHAT],
        "capabilities": [],
    },
    {
        "name": "deepseek-coder",
        "categories": [ModelCategory.LLM, ModelCategory.CHAT],
        "capabilities": [],
    }
]


def init_model(
    model: str, temperature: float, openai_api_key: str, openai_api_base: str, **kwargs
):
    model_info = next((m for m in SUPPORTED_MODELS if m["name"] == model), None)
    if model_info and ModelCategory.CHAT in model_info["categories"]:
        return ChatOpenAI(
            model=model,
            temperature=temperature,
            api_key=openai_api_key,
            base_url=openai_api_base,
            **kwargs,
        )
    else:
        raise ValueError(f"Model {model} is not supported as a chat model.")


def init_crewai_model(model: str, openai_api_key: str, openai_api_base: str, **kwargs):
    model_info = next((m for m in SUPPORTED_MODELS if m["name"] == model), None)
    if model_info and ModelCategory.CHAT in model_info["categories"]:
        return LLM(
            model=f"openai/{model}",  # CrewAI 格式：provider/model
            base_url=openai_api_base,
            api_key=openai_api_key,
            **kwargs,
        )
    else:
        raise ValueError(f"Model {model} is not supported as a chat model.")
