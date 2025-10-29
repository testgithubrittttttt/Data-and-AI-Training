import os
import requests
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory

# ------------------------------------------------------------
# 1. Load environment variables
# ------------------------------------------------------------

#This loads environment variables from a .env file into the Python environment. This is useful for keeping sensitive information (like API keys) out of your source code.
load_dotenv()

#Retrieves the value of OPENROUTER_API_KEY from the environment, which is assumed to be stored in a .env file. This key is likely needed to authenticate requests to an API (OpenRouter in this case).
api_key = os.getenv("OPENROUTER_API_KEY")
base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in .env file")

# ------------------------------------------------------------
# 2. Initialize the Mistral model via OpenRouter
# ------------------------------------------------------------
llm = ChatOpenAI(

    #Specifies that the agent will use a Mistral 7B Instruct model hosted on OpenRouter, presumably a variant of GPT-like models but with optimizations.
    model="mistralai/mistral-7b-instruct:free",

    #Controls randomness in the responses. Lower values (like 0.4) make the model’s output more deterministic, meaning less creative and more factual answers.
    temperature=0.4,

    #Sets the maximum number of tokens (words or word pieces) the model can generate in a single response. This is a way to limit the length of the agent's responses.
    max_tokens=256,
    api_key=api_key,
    base_url=base_url,
)


# ------------------------------------------------------------
# 3. Define helper tools
# ------------------------------------------------------------

def multiply(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b


def greet(name: str) -> str:
    """Return a friendly greeting."""
    name = name.strip().replace('"', "").replace("'", "")
    return f"Hello {name}, welcome to the AI Agent demo!"


def weather(city: str) -> str:
    """Return dynamic weather information for a given city using OpenWeatherMap API."""
    api_key = "2da986445cbd7426eaa4e912531dc575"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    city = city.strip().lower()  # Format the city name

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",  # Temperature in Celsius (change to "imperial" for Fahrenheit)
        "lang": "en"  # English response
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for bad responses

        data = response.json()

        if data.get("cod") != 200:
            return f"Sorry, I couldn't find the weather for {city.title()}. Please check the city name and try again."

        city_name = data["name"]
        weather_desc = data["weather"][0]["description"]
        temperature = data["main"]["temp"]

        return f"The current weather in {city_name.title()} is {weather_desc} with a temperature of {temperature}°C."

    except requests.exceptions.RequestException as e:
        return f"Sorry, there was an error fetching the weather information: {e}"


# ------------------------------------------------------------
# 4. Initialize memory
# ------------------------------------------------------------

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
# ConversationBufferMemory: This is a memory management class from the langchain library, used to keep track of previous conversations. This memory will store a buffer of user inputs and system responses so that the agent can recall the context of the conversation.
#
# memory_key="chat_history": This assigns the memory buffer a key, under which it will be stored in the agent's internal state.
#
# return_messages=True: This option ensures that the full sequence of conversation messages is returned, not just the most recent interaction.

# ------------------------------------------------------------
# 5. Conversational loop
# ------------------------------------------------------------
print("\n=== Start chatting with your Agent ===")
print("Type 'exit' to quit.\n")


# while True:: The main loop runs indefinitely, continuously asking for user input until exit is typed.
#
# input("You: ").strip(): This gets the user's input and strips any leading or trailing spaces to avoid accidental issues when processing the command.
#
# if user_input.lower() == "exit":: If the user types "exit", the loop breaks, and the conversation ends.
while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "exit":
        print("\nConversation ended.")
        break

    # Handle Multiply command
    if user_input.lower().startswith("multiply"):
        try:
            parts = user_input.split()#Splits the input string into components. For example, if the user typed "multiply 3 5", parts would become ["multiply", "3", "5"].
            a, b = int(parts[1]), int(parts[2])#Converts the second and third parts into integers and stores them in variables a and b.
            result = multiply(a, b)
            print("Agent:", result)
            memory.save_context({"input": user_input}, {"output": str(result)})#Saves the user input and the result into the conversation memory so the agent can keep track of the interaction.
            continue
        except Exception:
            print("Agent: Please use 'Multiply a b' format.")
            continue

    # Handle Greet command
    if user_input.lower().startswith("greet"):
        try:
            name = " ".join(user_input.split()[1:]).strip()
            
            if not name:
                print("Agent: Please specify a name. Example: greet Abdullah")
                continue
            greeting = greet(name)
            print("Agent:", greeting)
            memory.save_context({"input": user_input}, {"output": greeting})
            continue
        except Exception as e:
            print("Agent: Could not greet properly:", e)
            continue

    # Handle name introduction
    if "my name is" in user_input.lower():
        name = user_input.split("is")[-1].strip()
        memory.save_context({"input": user_input}, {"output": name})
        print("Agent:", greet(name))
        continue

    # Handle asking for name
    if "what" in user_input.lower() and "my name" in user_input.lower():
        messages = memory.load_memory_variables({}).get("chat_history", [])
        if messages:
            last_output = messages[-1].content
            print("Agent: You said your name is", last_output)
        else:
            print("Agent: I don't know your name yet.")
        continue

    # Handle weather command
    if user_input.lower().startswith("weather"):
        try:
            parts = user_input.split()
            city = " ".join(parts[1:]).strip()  # Extract city name
            if not city:
                print("Agent: Please specify a city. Example: weather Dubai")
                continue
            weather_info = weather(city)  # Call the dynamic weather function
            print("Agent:", weather_info)
            memory.save_context({"input": user_input}, {"output": weather_info})
            continue
        except Exception as e:
            print("Agent: Could not fetch weather information:", e)
            continue

    # Default: use LLM
    try:
        response = llm.invoke(user_input)
        print("Agent:", response.content)
        memory.save_context({"input": user_input}, {"output": response.content})
    except Exception as e:
        print("Error:", e)
