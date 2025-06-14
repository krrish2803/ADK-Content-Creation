# image_generation_agent.py
from pydantic import BaseModel, Field
from common_llm import llm_call

class ImageGenerationAgent(BaseModel):
    name: str = Field(default="ImageGenerationAgent")

    def generate_prompt(self, topic: str) -> dict:
        prompt = f"""
        Create a DALL-E compatible prompt to generate an image representing the topic: {topic}.
        Be descriptive.
        """
        result = llm_call(prompt)
        return {"image_prompt": result}