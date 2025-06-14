# orchestration.py
from pydantic import BaseModel, Field
from planner_agent import PlannerAgent
from research_agent import ResearchAgent
from content_generator_agent import ContentGenerator
from refinement_agent import RefinementAgent
from code_generation_agent import CodeGenerationAgent
from image_generation_agent import ImageGenerationAgent

class OrchestrationAgent(BaseModel):
    planner: PlannerAgent = Field(default_factory=PlannerAgent)
    researcher: ResearchAgent = Field(default_factory=ResearchAgent)
    content_generator: ContentGenerator = Field(default_factory=ContentGenerator)
    refiner: RefinementAgent = Field(default_factory=RefinementAgent)
    code_generator: CodeGenerationAgent = Field(default_factory=CodeGenerationAgent)
    image_generator: ImageGenerationAgent = Field(default_factory=ImageGenerationAgent)

    def run(self, topic: str, tone: str = "formal", language: str = "English") -> dict:
        plan_output = self.planner.plan(topic)
        research_output = self.researcher.research(topic)
        content_output = self.content_generator.generate(topic, research_output["research"])
        refined_output = self.refiner.refine(content_output["content"], tone, language)
        code_output = self.code_generator.generate_code(topic)
        image_prompt_output = self.image_generator.generate_prompt(topic)

        return {
            "plan": plan_output["plan"],
            "research": research_output["research"],
            "content": content_output["content"],
            "refined_content": refined_output["refined_content"],
            "code": code_output["code"],
            "image_prompt": image_prompt_output["image_prompt"]
        }

