import os
import json
from datetime import datetime
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage

# ----------------------------------------------------------
# 1. Load environment variables
# ----------------------------------------------------------
load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

if not api_key:
    raise ValueError("OPENROUTER_API_KEY missing in .env")

# ----------------------------------------------------------
# 2. Initialize model (Mistral via OpenRouter)
# ----------------------------------------------------------
llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct",
    temperature=0.7,
    max_tokens=512,
    api_key=api_key,
    base_url=base_url,
)

# ----------------------------------------------------------
# 3. Prompt template with context
# ----------------------------------------------------------
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly and concise teaching assistant. Keep explanations clear and short."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{topic}")
])

# ----------------------------------------------------------
# 4. Setup chain (LangChain 1.0 uses LCEL pipeline)
# ----------------------------------------------------------
parser = StrOutputParser()
chain = prompt | llm | parser

# ----------------------------------------------------------
# 5. Conversation memory setup
# ----------------------------------------------------------
chat_history = []  # stores HumanMessage and AIMessage objects
os.makedirs("logs", exist_ok=True)

print("\n=== AI Tutor (Mistral via OpenRouter) ===")
print("Context is preserved across turns. Type 'exit' to quit.\n")

# ----------------------------------------------------------
# 6. Chat loop
# ----------------------------------------------------------
while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "exit":
        print("\nGoodbye! 👋")
        break

    # Run the chain with context
    response = chain.invoke({
        "topic": user_input,
        "chat_history": chat_history
    })

    print(f"\nAI: {response}\n")

    # Save to memory
    chat_history.append(HumanMessage(content=user_input))
    chat_history.append(AIMessage(content=response))

    # Log the conversation
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "user": user_input,
        "assistant": response
    }
    with open("logs/conversation_log.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry) + "\n")

    print("(Context saved — you can refer to previous topics.)\n")
