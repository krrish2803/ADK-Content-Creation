# research_agent.py
from pydantic import BaseModel, Field
from common_llm import llm_call

class ResearchAgent(BaseModel):
    name: str = Field(default="ResearchAgent")

    def research(self, topic: str) -> dict:
        prompt = f"""
        Perform deep research on the topic: {topic}.
        Provide bullet points with insights, facts, and supporting data.
        """
        result = llm_call(prompt)
        return {"research": result}


