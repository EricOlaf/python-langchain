from dotenv import load_dotenv
import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

class HistoryQuiz:
    def __init__(self, llm=None):
        # Use OpenAI LLM by default, you can pass your own
        self.llm = llm or OpenAI(openai_api_key=api_key, temperature=0.7)
        self.question = None
        self.correct_answer = None

    def write_question(self, topic: str) -> str:
        """Generate a historical question with a date as the answer."""
        prompt = PromptTemplate(
            input_variables=["topic"],
            template="Write a simple history quiz question about {topic} where the answer is a specific year."
        )
        self.question = self.llm(prompt.format(topic=topic))
        return self.question

    def get_correct_answer(self) -> str:
        """Get the correct date answer from the LLM for the current question."""
        if not self.question:
            raise ValueError("No question has been generated yet.")
        prompt = PromptTemplate(
            input_variables=["question"],
            template="What is the correct year for the following history question? {question} Only respond with the year."
        )
        self.correct_answer = self.llm(prompt.format(question=self.question)).strip()
        return self.correct_answer

    def get_user_guess(self) -> str:
        """Prompt the human user for their best guess at the correct year."""
        guess = input(f"{self.question}\nYour answer (year): ").strip()
        return guess

    def check_answer(self, user_answer: str) -> str:
        """Report the difference between the correct answer and the user's answer."""
        try:
            correct_year = int(self.correct_answer)
            user_year = int(user_answer)
            diff = abs(correct_year - user_year)
            return f"Correct year: {correct_year}. Your answer: {user_year}. Difference: {diff} years."
        except ValueError:
            return "Invalid input. Please enter a valid year."

# Example usage:
quiz = HistoryQuiz()
quiz.write_question("the fall of the Berlin Wall")
quiz.get_correct_answer()
user_guess = quiz.get_user_guess()
print(quiz.check_answer(user_guess))