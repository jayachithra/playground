"""Meeseeks AI chatbot"""
from .openai_client import AzureOpenAIClient
from .personas import GeneralQA
from .orchestrator import Orchestrator

def chat():
    """Interact with the user"""
    orchestrator = Orchestrator(AzureOpenAIClient(), GeneralQA())
    while True:
        user_prompt = input("Q: ")
        
        if user_prompt == "quit":
            break
        
        message = orchestrator.get_response(user_prompt)
        print(f"A: {message}")
        
# Todo
# - Store history in a local database
# - Use langchain to summarize the chat history
# - Use langchain to generate a response

def main():
    """"Entry point"""
    print("Welcome to Meeseeks AI chatbot!")
    print("Type 'quit' to exit the chatbot.")
           
    chat()
