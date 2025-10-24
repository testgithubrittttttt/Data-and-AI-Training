import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

# 1. Load environment variables from .env
load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in .env file")

def get_response(user_input: str, model: str) -> str:
    messages = [
        SystemMessage(content="You are a helpful and concise AI assistant."),
        HumanMessage(content=f"[INST] {user_input} [/INST]"),
    ]

    llm = ChatOpenAI(
        model=model,
        temperature=0.7,
        max_tokens=256,
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url=os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1"),
    )

    try:
        response = llm.invoke(messages)
        return response.content.strip().replace("<s>", "") or "(no content returned)"
    except Exception as e:
        return f"Error: {e}"


# # 2. Initialize LangChain model pointing to OpenRouter
# llm = ChatOpenAI(
#     model="mistralai/mistral-7b-instruct",
#     temperature=0.7,
#     max_tokens=256,
#     api_key=api_key,
#     base_url=base_url,
# )
#
# def get_response(user_input: str) -> str:
#     messages = [
#         SystemMessage(content="You are a helpful and concise AI assistant."),
#         HumanMessage(content=f"[INST] {user_input} [/INST]"),
#     ]
#     try:
#         response = llm.invoke(messages)
#         response_text = response.content.replace("<s>", "")
#
#         return response_text.strip() or "(no content returned)"
#     except Exception as e:
#         return f"Error: {e}"

