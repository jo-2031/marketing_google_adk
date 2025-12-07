import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROMPTS_DIR = os.path.join(BASE_DIR, "config", "prompts")
DEFAULT_USER_ID = "user123"
DEFAULT_APP_NAME = "marketing_pipeline" 
DEFAULT_SESSION_ID = "marketing_session"
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")