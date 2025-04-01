import os

# Configuration settings
os.environ["GROQ_API_KEY"] = "your api"

LLM_CONFIG = {
    "model": "llama-3.1-8b-instant",
    "temperature": 0,
    "max_tokens": None,
    "timeout": None,
    "max_retries": 2
}