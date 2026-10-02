from langchain_openai import ChatOpenAI, OpenAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv(override=True)

api_key = os.getenv("LLM_API_KEY")
BASE_URL = os.getenv("BASE_URL")
# print(api_key)

def llm_connect(
    model: str,
    api_key: str = api_key,
    temperature: float = 0,
    max_tokens: int = 512
):
    return ChatOpenAI(
        model=model,
        api_key=api_key,
        base_url=BASE_URL,
        temperature=temperature,
        use_responses_api=False,  # base url로 할 때는 이부분 넣어야 함.(MonoRouter 사용)
        max_tokens=max_tokens,
    )
    
def embedding_model():
    embedding_model = "text-embedding-3-small"
    embeddings = OpenAIEmbeddings(
        api_key=api_key,
        base_url=BASE_URL,
        model=embedding_model
        )
    
    return embeddings