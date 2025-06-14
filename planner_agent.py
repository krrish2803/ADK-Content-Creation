# planner_agent.py
from pydantic import BaseModel, Field
from common_llm import llm_call

class PlannerAgent(BaseModel):
    name: str = Field(default="PlannerAgent")

    def plan(self, topic: str) -> dict:
        prompt = f"""
        Create a high-level content plan for the topic: {topic}.
        Include key research areas, structure, tone, and output types (e.g., text, code, images).
        """
        result = llm_call(prompt)
        return {"plan": result, "topic": topic}

