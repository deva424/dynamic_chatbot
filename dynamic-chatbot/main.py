import os
from dotenv import load_dotenv
from src.chatbot.engine import ask_chatbot

# Load API keys
load_dotenv()

def run_chat():
    print("--- Dynamic AI Knowledge Assistant ---")
    print("Type 'exit' to quit.")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            break
            
        try:
            response = ask_chatbot(user_input)
            print(f"\nAI: {response}")
        except Exception as e:
            print(f"\nError: {e}. (Ensure the vector database has been initialized by the scheduler first!)")

if __name__ == "__main__":
    run_chat()