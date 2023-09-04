from abc import ABC, abstractmethod


class Persona(ABC):
    """Abstract class for personas"""
    def __init__(self):
        """Initialize the persona"""
        self.system_message = None
    
    @abstractmethod
    def get_system_message(self):
        """Get the system message"""
        pass

class GeneralQA(Persona):
    """Meeseeks AI chatbot persona"""
    def __init__(self):
        """Initialize the persona"""
        self.system_message = "You are a friendly AI assistant called Meeseeks. Always introduce yourself to the user. Your job is to help users with their queries."
    
    def get_system_message(self):
        """Get the system message"""
        return self.system_message

# To do: other personas with RAG