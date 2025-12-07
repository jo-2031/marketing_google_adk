from google.adk import Runner
from google.adk.sessions import InMemorySessionService
from ai_agents.root_agent import PipelineManager
from config.settings import DEFAULT_USER_ID, DEFAULT_APP_NAME
import uuid

class SessionMemory:
    def __init__(self):
        self.root_agent = PipelineManager().get_agent()  
        self.session_service = InMemorySessionService()
        self.runner = Runner(
            agent=self.root_agent,                  
            session_service=self.session_service,
            app_name=DEFAULT_APP_NAME
        )

    async def create_fresh_session(self):
        """
        Create a new session with a unique ID to avoid previous memory influence.
        """
        session_id = str(uuid.uuid4())
        await self.session_service.create_session(
            user_id=DEFAULT_USER_ID,
            app_name=DEFAULT_APP_NAME,
            session_id=session_id
        )
        return session_id

    def run_async(self, **kwargs):
        return self.runner.run_async(**kwargs)
