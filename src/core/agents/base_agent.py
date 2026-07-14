from abc import ABC

from core.llm.llm_client import LLMClient

class BaseAgent(ABC):

    """
    BAse class for all AI agents.
    Responsibilities:
    -Receive a task.
    -Delegate text generation to an LLM
    -Return the generated response.

    Future versions will support:
    -Memory
    -Tools
    -Planning
    -Workflows
    """
    
    def __init__(self, llm:LLMClient):
        self._llm = llm
    
    def run (self, task: str) -> str:
        """
        Execute a task using the configured LLM.
        """
    