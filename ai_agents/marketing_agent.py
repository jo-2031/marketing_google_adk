from google.adk.agents import  LlmAgent
from schemas.marketing_schema import MarketingOutput
from utils.file_load import load_prompt
from google.adk.agents import BaseAgent
from google.adk.models.lite_llm import LiteLlm


class MarketingAgent:
    def __init__(self):
        pass

    def run(self):
        marketing_agent = LlmAgent(
        name="MarketingAgent",
        model=LiteLlm(model="openai/gpt-4o"),
        instruction=load_prompt("marketing_prompt.txt"),
        tools=[MarketingOutput]
    )
        return marketing_agent
    