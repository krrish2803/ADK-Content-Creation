# content_generator_agent.py
from pydantic import BaseModel, Field
from common_llm import llm_call

class ContentGenerator(BaseModel):
    name: str = Field(default="ContentGenerator")

    def generate(self, topic: str, research: str) -> dict:
        prompt = f"""
        Write detailed content on: {topic}.
        Use the following research:
        {research}
        Make the content informative and engaging.
        """
        result = llm_call(prompt)
        return {"content": result}
