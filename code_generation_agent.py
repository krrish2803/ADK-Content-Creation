# code_generation_agent.py
from pydantic import BaseModel, Field
from common_llm import llm_call

class CodeGenerationAgent(BaseModel):
    name: str = Field(default="CodeGenerationAgent")

    def generate_code(self, topic: str) -> dict:
        prompt = f"""
        Generate a Python code snippet that demonstrates the topic: {topic}.
        Include comments and explanations.
        """
        result = llm_call(prompt)
        return {"code": result}
