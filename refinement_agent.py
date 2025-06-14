
# refinement_agent.py
from pydantic import BaseModel, Field
from common_llm import llm_call

class RefinementAgent(BaseModel):
    name: str = Field(default="RefinementAgent")

    def refine(self, content: str, tone: str = "formal", language: str = "English") -> dict:
        prompt = f"""
        Improve the content below:
        - Ensure it is in a {tone} tone
        - Translate or adjust to {language} if needed
        - Fix grammar, readability, and clarity

        Content:
        ---
        {content}
        ---
        Return markdown format.
        """
        result = llm_call(prompt)
        return {"refined_content": result}

