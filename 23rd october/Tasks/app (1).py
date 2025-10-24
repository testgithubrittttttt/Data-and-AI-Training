# import streamlit as st
# from GenAI import get_response
#
# # Page config
# st.set_page_config(page_title="✨ Chat with AI", layout="centered")
#
# # Custom CSS for cuteness overload
# st.markdown("""
#     <style>
#     html, body, [class*="css"]  {
#         font-family: 'Comic Sans MS', cursive, sans-serif;
#         background-color: #fffafc;
#     }
#     .chat-bubble {
#         padding: 1em;
#         margin: 0.5em 0;
#         border-radius: 1em;
#         max-width: 80%;
#         word-wrap: break-word;
#     }
#     .user-bubble {
#         background-color: #d0f0fd;
#         align-self: flex-end;
#         margin-left: auto;
#     }
#     .ai-bubble {
#         background-color: #ffe0f0;
#         align-self: flex-start;
#         margin-right: auto;
#     }
#     </style>
# """, unsafe_allow_html=True)
#
# # Title
# st.markdown("<h1 style='text-align: center;'>🧠💬 Chat with Your AI BFF</h1>", unsafe_allow_html=True)
#
# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []
#
# # Display chat bubbles
# for msg in st.session_state.messages:
#     bubble_class = "user-bubble" if msg["role"] == "user" else "ai-bubble"
#     st.markdown(f"<div class='chat-bubble {bubble_class}'>{msg['content']}</div>", unsafe_allow_html=True)
#
# # Chat input
# user_input = st.chat_input("Type something sweet...")
#
# if user_input:
#     st.session_state.messages.append({"role": "user", "content": user_input})
#     st.markdown(f"<div class='chat-bubble user-bubble'>{user_input}</div>", unsafe_allow_html=True)
#
#     with st.spinner("Sprinkling magic... ✨"):
#         response = get_response(user_input)
#
#     st.session_state.messages.append({"role": "assistant", "content": response})
#     st.markdown(f"<div class='chat-bubble ai-bubble'>{response}</div>", unsafe_allow_html=True)
import streamlit as st
from GenAI import get_response

# Page config
st.set_page_config(page_title="✨ Chat with AI", layout="centered")

# Sidebar: Model selector
st.sidebar.header("🧠 Choose Your AI Model")
model_choice = st.sidebar.selectbox(
    "Pick a free model:",
    options=[
        "mistralai/mistral-small-3.2-24b-instruct:free",
        "mistralai/mistral-small-3.1-24b-instruct:free",
        "mistralai/devstral-small-2505:free",
        "z-ai/glm-4.5-air:free",
    ],
    index=0,
    help="These are free models available via OpenRouter"
)

# Store model in session state
st.session_state["selected_model"] = model_choice

# Custom CSS for cuteness
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        font-family: 'Comic Sans MS', cursive, sans-serif;
        background-color: #fffafc;
    }
    .chat-bubble {
        padding: 1em;
        margin: 0.5em 0;
        border-radius: 1em;
        max-width: 80%;
        word-wrap: break-word;
    }
    .user-bubble {
        background-color: #d0f0fd;
        align-self: flex-end;
        margin-left: auto;
    }
    .ai-bubble {
        background-color: #ffe0f0;
        align-self: flex-start;
        margin-right: auto;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("""
    <div style='text-align: center; padding: 1rem 0;'>
        <h1 style='font-size: 2.5rem; color: #ff69b4;'>🧠💬 Chat with Your AI BFF</h1>
    </div>
""", unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat bubbles
for msg in st.session_state.messages:
    bubble_class = "user-bubble" if msg["role"] == "user" else "ai-bubble"
    st.markdown(f"<div class='chat-bubble {bubble_class}'>{msg['content']}</div>", unsafe_allow_html=True)

# Chat input
user_input = st.chat_input("Type something sweet...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.markdown(f"<div class='chat-bubble user-bubble'>{user_input}</div>", unsafe_allow_html=True)

    with st.spinner("Sprinkling magic... ✨"):
        response = get_response(user_input, model=st.session_state["selected_model"])

    st.session_state.messages.append({"role": "assistant", "content": response})
    st.markdown(f"<div class='chat-bubble ai-bubble'>{response}</div>", unsafe_allow_html=True)
