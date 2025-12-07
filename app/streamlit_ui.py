import streamlit as st
import sys
import os
import tempfile
import asyncio
import nest_asyncio
import json

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from orchestrator.pipeline_workflow import Workflow
from utils.file_load import clean_json_string  # import your helper

# Fix nested event loop issues (important for Streamlit + asyncio)
nest_asyncio.apply()

# Initialize workflow once
workflow = Workflow()


def main():
    # Streamlit Page Settings
    st.set_page_config(page_title="Marketing AI Pipeline", layout="centered")

    # --- UI ---
    st.title("📸 AI Marketing Pipeline")
    st.write("Upload an image and choose a brand voice to generate marketing outputs.")

    uploaded_file = st.file_uploader("Upload Product Image", type=["jpg", "jpeg", "png"])
    brand_voice = st.text_input("Brand Voice", value="Energetic and modern")

    run_button = st.button("Generate Marketing Output")

    # --- Pipeline Execution ---
    if run_button:
        if not uploaded_file:
            st.error("❌ Please upload an image first.")
            st.stop()

        # Save the uploaded image temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
            tmp.write(uploaded_file.read())
            temp_image_path = tmp.name

        st.info("⏳ Running pipeline... please wait...")

        try:
            # Execute async pipeline properly
            loop = asyncio.get_event_loop()
            result = loop.run_until_complete(
                workflow.run_pipeline(temp_image_path, brand_voice)
            )

            # Clean the result if it contains Markdown fences
            if isinstance(result, str):
                clean_result = clean_json_string(result)
                try:
                    result = json.loads(clean_result)
                except json.JSONDecodeError as e:
                    st.error(f"❌ JSON parse error: {e}")
                    st.stop()

            st.success("✅ Pipeline completed successfully!")
            st.subheader("📦 Final Output (Structured JSON)")

            # Pretty JSON output box
            st.json(result)

        except Exception as e:
            st.error(f"🚨 Pipeline error: {e}")

        finally:
            # Clean up temporary file
            if os.path.exists(temp_image_path):
                os.remove(temp_image_path)


if __name__ == "__main__":
    main()
