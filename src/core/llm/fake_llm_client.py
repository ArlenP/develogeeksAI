from core.llm.llm_client import LLMClient

class FakeLLMClient(LLMClient):
    """ 
    Fake implementation of an LLM

    Useful for:
    -Developing the architecture.
    -Unit Tests.
    -Running the project without an extenal LLM.
    
    """
    def generate(self, promt: str) -> str:
        return (
            "======== Fake LLM REsponse======\n"
            f"Prompt received: \n{prompt}\n"
            "==============================="
        )