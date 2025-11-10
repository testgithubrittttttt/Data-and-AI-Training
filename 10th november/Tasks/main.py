from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from .openrouter_client import ask_openrouter

app = FastAPI(title="AI QnA Bot — FastAPI + OpenRouter")

# Allow Streamlit to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all for local dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(q: Query):
    """
    Takes a natural-language question and returns an AI-generated answer from OpenRouter.
    """
    try:
        answer = ask_openrouter(q.question)
        return {"question": q.question, "answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "ok"}
