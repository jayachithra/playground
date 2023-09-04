# Client to interact with OpenAI's API
import os
import openai
from abc import ABC
from dotenv import load_dotenv

class OpenAIClient(ABC):
    def __init__(self) -> None:
        pass

class AzureOpenAIClient(OpenAIClient):
    """Client to interact with OpenAI's API"""
    def __init__(self):
        """Initialize the OpenAIClient"""
        load_dotenv()
        if not os.environ.get("OPENAI_API_KEY") or not os.environ.get("OPENAI_API_BASE"):
            openai_api_key = input("Please enter the openai api key: ")
            openai_api_base = input("Please enter the openai api base: ")

            os.environ["OPENAI_API_KEY"] = openai_api_key
            os.environ["OPENAI_API_BASE"] = openai_api_base

        self.api_key = os.environ["OPENAI_API_KEY"]
        self.api_base = os.environ["OPENAI_API_BASE"]
        self.api_type = "azure"
        self.api_version = "2023-03-15-preview"
        openai.api_key = self.api_key
        openai.api_base = self.api_base
        openai.api_type = self.api_type
        openai.api_version = self.api_version

    def get_chat_completion(self, messages, engine="gpt-35-turbo", model="gpt-35-turbo", temperature=0):
        response = openai.ChatCompletion.create(engine=engine, model=model, messages=messages, temperature=temperature)
        return response.choices[0].message.content