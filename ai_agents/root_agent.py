# agents/root_agent.py
from ai_agents.image_agent import ImageAgent
from ai_agents.marketing_agent import MarketingAgent
from ai_agents.seo_agent import SEOAgent
from google.adk.agents import SequentialAgent

class PipelineManager:
    def __init__(self):

        self.image_agent = ImageAgent().run()      
        self.marketing_agent = MarketingAgent().run()
        self.seo_agent = SEOAgent().run()

        # Sequential agent containing all sub-agents
        self.pipeline_agent = SequentialAgent(
            name="MarketingPipelineAgent",
            sub_agents=[self.image_agent, self.marketing_agent, self.seo_agent],
            description="Analyzes an image, generates marketing content, SEO, and upsells sequentially. "
                "The output must be ONLY the structured JSON object matching the expected schemas. "
                "Do not include greetings, confirmations, or any extra text. "
                "Each sub-agent should produce its JSON, and the final output must be a combined JSON string."
        )

    def get_agent(self):
        # return the actual SequentialAgent
        return self.pipeline_agent
