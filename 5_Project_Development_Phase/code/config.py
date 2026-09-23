import os
from pathlib import Path
from dotenv import load_dotenv

# Base Directory of LegalEase
BASE_DIR = Path(__file__).resolve().parent

# Load environment variables from .env file
load_dotenv(BASE_DIR / ".env")

# API and Server Configuration
API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", 8000))
API_BASE_URL = os.getenv("API_BASE_URL", f"http://localhost:{API_PORT}")

# Google Gemini AI Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-pro")

# Branding Assets
IMAGE_DIR = BASE_DIR / "image"
LOGO_PATH = IMAGE_DIR / "Logo.png"
INVERSE_LOGO_PATH = IMAGE_DIR / "inverseLogo.png"
WEB_LOGO_PATH = INVERSE_LOGO_PATH if INVERSE_LOGO_PATH.exists() else LOGO_PATH
