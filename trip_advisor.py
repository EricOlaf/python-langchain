from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# Load env variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the model
llm = ChatOpenAI(openai_api_key=api_key, temperature=0.7)

# Add conversational memory
memory = ConversationBufferMemory()

# Set up the chatbot chain
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

user_interest = input("Enter your interest (e.g., nature, history, food): ")
user_budget = input("Enter your budget (e.g., low, medium, high): ")
user_duration = input("Enter your trip duration in days: ")

def trip_advisor(interest, budget, duration):
    if user_interest and user_budget and user_duration:
        prompt = f"Plan a trip for someone interested in {interest}, with a budget of {budget}, and a duration of {duration} days."
        response = conversation.predict(input=prompt)
        print(f"AI: {response}\n")
    else:
        print("Please restart and provide all the required information.")

trip_advisor(user_interest, user_budget, user_duration)
