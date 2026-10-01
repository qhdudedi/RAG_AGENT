import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv(override=True)

BASE_URL = os.getenv("BASE_URL")
API_KEY_ENV = "LLM_API_KEY"

DEFAULT_TEMPERATURE = 0.0
DEFAULT_MAX_TOKENS = 512


def _get_api_key() -> str:
    key = os.getenv(API_KEY_ENV)
    if not key:
        raise ValueError(f"API 키가 없습니다. .env에 {API_KEY_ENV}를 설정하세요.")
    return key


def llm_connect(
    model: str,
    temperature: float = 0,
    max_tokens: int = 512,
) -> ChatOpenAI:
    
    return ChatOpenAI(
        model=model,
        api_key=_get_api_key(),
        base_url=BASE_URL,
        temperature=temperature,
        max_tokens=max_tokens,
        use_responses_api=False,

    )
