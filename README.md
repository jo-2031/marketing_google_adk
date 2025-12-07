# Marketing AI Pipeline

An advanced multi-agent AI pipeline for e-commerce marketing. This system uses **image analysis, marketing content generation, and SEO optimization** in a sequential pipeline to process product images and generate structured marketing-ready outputs. Built using **Google ADK**, LLM models (e.g., OpenAI/Gemini), and **Streamlit** for the UI.

---

## Features

- **Image Analysis Agent**: Identifies the product in a provided image and generates structured product info.
- **Marketing Agent**: Creates marketing-ready taglines, short and long descriptions, aligned with brand voice.
- **SEO Agent**: Generates SEO keywords, ad copies, and upsell product suggestions.
- **Sequential Agent Pipeline**: Combines all agents to run in a step-by-step flow.
- **Streamlit UI**: Upload product images and brand voice, get final JSON outputs instantly.
- **Supports any product category**: Electronics, fashion, home goods, beauty, toys, books, food, and more.

---

## Project Structure

```
marketing-ai-pipeline/
│
├─ app/
│   ├─ __init__.py
│   └─ streamlit_ui.py        # Streamlit interface
│
├─ ai_agents/
│   ├─ __init__.py
│   ├─ image_agent.py         # Image analysis agent
│   ├─ marketing_agent.py     # Marketing agent
│   ├─ seo_agent.py           # SEO agent
│   └─ root_agent.py          # Sequential agent combining all
│
├─ orchestrator/
│   ├─ __init__.py
│   ├─ workflow.py            # Async pipeline workflow
│   └─ session_memory.py      # Handles fresh session creation
│
├─ schemas/
│   ├─ __init__.py
│   ├─ marketing_Schema.py
│   ├─ product_info.py
│   └─ seo_Schema.py
│
├─ utils/
│   ├─ __init__.py
│   ├─ image_processing.py    # Base64 encoding helper
│   └─ file_load.py           # JSON/text loading helper
│
├─ config/
│   ├─ __init__.py
│   ├─ settings.py            # API keys, defaults, app name
│   └─ prompts/
│       ├─ image_prompt.txt
│       ├─ marketing_prompt.txt
│       └─ seo_prompt.txt
│
├─ requirements.txt           # Python dependencies
└─ README.md                  # This file
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd marketing-ai-pipeline
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

**Activate the environment:**

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```

- **macOS / Linux:**
  ```bash
  source venv/bin/activate
  ```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API keys

Edit `config/settings.py`:

```python
DEFAULT_USER_ID = "<your_user_id>"
DEFAULT_APP_NAME = "MarketingAI"
OPENAI_API_KEY = "<your_openai_api_key>"
```

If using Google Gemini via `genai`, configure credentials accordingly.

### 5. Add prompts (optional)

Modify prompts in `config/prompts/`:

- `image_prompt.txt` – prompt template for the Image Agent
- `marketing_prompt.txt` – prompt template for the Marketing Agent
- `seo_prompt.txt` – prompt template for the SEO Agent

### 6. Run Streamlit UI

```bash
streamlit run app/streamlit_ui.py
```

**Usage:**

1. Upload your product image
2. Provide brand voice (e.g., "Energetic and modern")
3. Click **Generate Marketing Output**
4. View structured JSON outputs for the product, marketing content, and SEO suggestions

---

## Technologies Used

- **Python 3.8+**
- **Streamlit** - Interactive web UI
- **Google ADK** - Agent orchestration framework
- **OpenAI / Google Gemini** - LLM models for content generation
- **Pydantic** - Data validation and schema management
- **Asyncio** - Asynchronous workflow execution
