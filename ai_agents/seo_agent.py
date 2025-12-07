from google.adk.agents import  LlmAgent
from schemas.seo_schema import SEOOutput
from utils.file_load import load_prompt
from google.adk.agents import BaseAgent
from google.adk.models.lite_llm import LiteLlm


class SEOAgent:
    def __init__(self):
        pass

    def run(self):
        seo_agent = LlmAgent(
        name="SEOAgent",
        model=LiteLlm(model="openai/gpt-4o"),
        instruction=load_prompt("seo_prompt.txt"),
        tools=[SEOOutput]
    )
        return seo_agent