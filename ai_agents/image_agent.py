from google.adk.agents import  LlmAgent
from schemas.product_info import ProductInfo
from utils.file_load import load_prompt
from google.adk.models.lite_llm import LiteLlm


class ImageAgent:
    def __init__(self):
        # if nothing needed, leave init empty
        pass
    def run(self):
        
        image_agent = LlmAgent(
            name="ImageAgent",
            model=LiteLlm(model="openai/gpt-4o"),
            instruction=load_prompt("image_prompt.txt"),
            tools=[ProductInfo]
        )
        return image_agent