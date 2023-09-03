class Orchestrator:
    def __init__(self, openaiclient, persona):
        self._openaiclient = openaiclient
        self._history = [{'role':'system', 'content': persona.get_system_message()}]

    def get_response(self, user_message: str) -> None:
        # Append user message to history
        self._history.append({'role':'user', 'content': user_message})

        # get chat completion
        chat_completion = self._openaiclient.get_chat_completion(self._history)

        # Append assistant message to history
        self._history.append({'role':'assistant', 'content': chat_completion})

        return chat_completion