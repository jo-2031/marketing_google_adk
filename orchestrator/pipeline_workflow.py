# orchestrator/workflow.py
import base64
import uuid
from google.genai import types
from google.adk import Runner
from google.adk.sessions import InMemorySessionService
from config.settings import DEFAULT_USER_ID, DEFAULT_APP_NAME
from ai_agents.root_agent import PipelineManager
from utils.image_processor import encode_image_to_base64

class Workflow:
    async def run_pipeline(self, image_file, brand_voice: str):
        """
        Run AI pipeline for a single image with a fresh session.
        
        Args:
            image_file: file-like object (Streamlit UploadedFile)
            brand_voice: string describing the brand tone
        Returns:
            str: JSON string returned by the pipeline
        """

        # --- 1. Fresh agent and runner ---
        pipeline_manager = PipelineManager()
        root_agent = pipeline_manager.get_agent()  # SequentialAgent
        session_service = InMemorySessionService()
        runner = Runner(agent=root_agent, session_service=session_service, app_name=DEFAULT_APP_NAME)

        # --- 2. Create a fresh session ---
        session_id = str(uuid.uuid4())
        await session_service.create_session(
            user_id=DEFAULT_USER_ID,
            app_name=DEFAULT_APP_NAME,
            session_id=session_id
        )

        # --- 3. Encode image to Base64 ---
        image_b64 = encode_image_to_base64(image_file)
        # --- 4. Decode Base64 to bytes for Google GenAI Part ---
        image_bytes = base64.b64decode(image_b64)

        # --- 5. Create Parts for the prompt ---
        image_part = types.Part.from_bytes(
            data=image_bytes,
            mime_type="image/png"  # or image/jpeg depending on your upload
        )

        text_part = types.Part(
            text=f"Analyze this product image in a '{brand_voice}' brand voice. "
                 "Return ONLY valid JSON describing the main product visible."
        )

        content = types.Content(
            role="user",
            parts=[text_part, image_part]
        )

        # --- 6. Run pipeline asynchronously ---
        final_result = None
        async for event in runner.run_async(
            user_id=DEFAULT_USER_ID,
            session_id=session_id,
            new_message=content
        ):
            if event.is_final_response() and event.content and event.content.parts:
                final_result = event.content.parts[0].text
                break

        return final_result
