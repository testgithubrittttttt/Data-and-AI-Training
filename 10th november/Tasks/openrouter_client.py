from dotenv import load_dotenv
import os
import requests

# Load the .env from the app directory explicitly
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

DEFAULT_MODEL = "openai/gpt-3.5-turbo"

def ask_openrouter(prompt: str, model: str = DEFAULT_MODEL) -> str:
    if not OPENROUTER_API_KEY:
        raise ValueError("Missing OpenRouter API key! Set it in the .env file or as environment variable.")

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant answering clearly and concisely."},
            {"role": "user", "content": prompt},
        ],
    }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    res = response.json()
    return res["choices"][0]["message"]["content"].strip()
