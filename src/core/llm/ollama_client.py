from .llm_client import LLMClient

class OllamaClient(LLMClient):

    def __init__(self, model:str):
        self.model = model
    
    def generate(self, promt: str) -> str:
        raise NotImplementedError(
            "Ollama integration not implemented yet"
        )