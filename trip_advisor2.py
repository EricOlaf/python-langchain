from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

def load_api_key():
    """Load OpenAI API key from environment variables."""
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in .env file.")
    return api_key

def init_chat_model(api_key: str) -> ConversationChain:
    """Initialize LangChain conversation model with memory."""
    llm = ChatOpenAI(openai_api_key=api_key, temperature=0.7)
    memory = ConversationBufferMemory()
    return ConversationChain(llm=llm, memory=memory, verbose=True)

def collect_user_preferences() -> tuple:
    """Collect trip preferences from user input."""
    interest = input("Enter your interest (e.g., nature, history, food): ").strip()
    budget = input("Enter your budget (e.g., low, medium, high): ").strip()
    duration = input("Enter your trip duration in days: ").strip()

    if not (interest and budget and duration):
        raise ValueError("All inputs are required. Please restart and provide complete information.")

    if not duration.isdigit():
        raise ValueError("Duration must be a number (in days).")

    return interest, budget, int(duration)

def generate_trip_plan(conversation: ConversationChain, interest: str, budget: str, duration: int):
    """Use LLM to generate a custom trip plan."""
    prompt = (
        f"Plan a personalized trip for someone who enjoys {interest}, "
        f"has a {budget} budget, and wants to travel for {duration} days. "
        f"Include destination ideas, activities, and any helpful tips."
    )
    response = conversation.predict(input=prompt)
    print("\n🧳 Your Custom AI Trip Plan:")
    print(response)

def main():
    try:
        api_key = load_api_key()
        conversation = init_chat_model(api_key)
        interest, budget, duration = collect_user_preferences()
        generate_trip_plan(conversation, interest, budget, duration)
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()