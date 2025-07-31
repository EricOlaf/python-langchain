from dotenv import load_dotenv
import os
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Create the LLM instance
llm = ChatOpenAI(openai_api_key=api_key, temperature=0.7)

# Run the model with a prompt
response = llm([HumanMessage(content="Here is a fun fact about Idaho:")])

print(response.content)