"""
Application configuration.

Loads environment variables from .env
and exposes them throughout the project.
"""

from pathlib import Path
from dotenv import load_dotenv
import os

# -------------------------------------------------------
# Load .env
# -------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(BASE_DIR / ".env")


# -------------------------------------------------------
# Application Settings
# -------------------------------------------------------

APP_NAME = os.getenv("APP_NAME", "ResearchOS")

DEBUG = os.getenv("DEBUG", "True") == "True"

HOST = os.getenv("HOST", "127.0.0.1")

PORT = int(os.getenv("PORT", 8000))


# -------------------------------------------------------
# Models
# -------------------------------------------------------

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "sentence-transformers/all-MiniLM-L6-v2"
)

CROSS_ENCODER_MODEL = os.getenv(
    "CROSS_ENCODER_MODEL",
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)
GROQ_MODEL = os.getenv(
    "GROQ_MODEL",
    "llama-3.3-70b-versatile"
)
RERANK_MODEL = os.getenv(
    "RERANK_MODEL",
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)

LLM_MODEL = os.getenv(
    "LLM_MODEL",
    "llama-3.3-70b-versatile"
)


# -------------------------------------------------------
# API Keys
# -------------------------------------------------------

GROQ_API_KEY = os.getenv(
    "GROQ_API_KEY"
)