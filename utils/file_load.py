import os
import json
import re
from config.settings import PROMPTS_DIR

def load_prompt(filename):
    path = os.path.join(PROMPTS_DIR, filename)
    with open(path, "r") as f:
        return f.read()
    
def clean_json_string(s):
    """
    Remove Markdown code fences (``` or ```json) from AI output
    and return a clean JSON string.
    """
    # Remove ``` or ```json at the start
    s = re.sub(r"^```(json)?", "", s.strip())
    # Remove ``` at the end
    s = re.sub(r"```$", "", s.strip())
    return s.strip()

