from abc import ABC, abstractmethod

class LLMClient(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Generates a response from an LLM
        """
        pass