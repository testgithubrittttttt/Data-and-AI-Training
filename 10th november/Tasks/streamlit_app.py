import streamlit as st
import requests

# FastAPI backend URL
BACKEND_URL = "http://127.0.0.1:8000/ask"

st.set_page_config(page_title="AI QnA Bot", layout="centered")

st.title("🤖 AI QnA Bot (FastAPI + OpenRouter + Streamlit)")
st.markdown(
    "Ask me anything — maths, dates, or words — and I’ll give you an answer using **OpenRouter LLM**."
)

# User input area
question = st.text_area(
    "Enter your question below:",
    placeholder="e.g., Add 45 and 35, Reverse the word Abdullah, What’s today’s date?",
)

if st.button("Submit"):
    if not question.strip():
        st.warning("Please type a question first.")
    else:
        with st.spinner("Thinking... 🧠"):
            try:
                response = requests.post(BACKEND_URL, json={"question": question})
                if response.status_code == 200:
                    data = response.json()
                    st.success(" Answer:")
                    st.markdown(f"**{data['answer']}**")
                else:
                    st.error(f" Error: {response.text}")
            except Exception as e:
                st.error(f"Connection error: {e}")

st.divider()
st.caption("Built with ❤ using Streamlit + FastAPI + OpenRouter")
