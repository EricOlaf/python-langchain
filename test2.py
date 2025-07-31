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

# Chat loop
print("🤖 Chatbot is ready! Type 'exit' to stop.\n")
while True:
    user_input = input("You: ")
    if user_input.lower() in {"exit", "quit"}:
        break
    response = conversation.predict(input=user_input)
    print(f"AI: {response}\n")