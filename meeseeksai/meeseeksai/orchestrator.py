from .openai_client import OpenAIClient
from .personas import Persona
from .helpers import get_tokens_from_message

MAX_TOKENS = 1000

class Orchestrator:
    def __init__(self, openaiclient: OpenAIClient, persona: Persona):
        self._openaiclient = openaiclient
        self._history = [{'role':'system', 'content': persona.get_system_message()}]

    def get_response(self, user_message: str) -> None:
        # Append user message to history
        self._history.append({'role':'user', 'content': user_message})

        # Truncate history to MAX_TOKENS by removing the oldest messages
        memory = self.truncate_history(self._history.copy())
        # For a chat completion, the memory should always be a list

        # get chat completion
        chat_completion = self._openaiclient.get_chat_completion(memory)

        # Append assistant message to history
        self._history.append({'role':'assistant', 'content': chat_completion})

        return chat_completion

    def truncate_history(self, history):
        num_tokens = get_tokens_from_message(history)
        while num_tokens > MAX_TOKENS:
            history.pop(1) # never pop system message
            num_tokens = self.get_tokens_from_message(history)
        return history
