import sys
from pathlib import Path

# Ensure root directory is on sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from legalEaseAPI.routes import router
from config import API_HOST, API_PORT

app = FastAPI(
    title="LegalEase - AI Legal Document Generator",
    description="Automated AI-powered legal document generation service using Google Gemini",
    version="1.0.0"
)

# Enable CORS for frontend and external integrations
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(router)

@app.get("/")
def home():
    """Health check and root route"""
    return {
        "message": "Welcome to LegalEase AI Legal Document Generator API",
        "status": "online",
        "version": "1.0.0",
        "documentation": "/docs"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("legalEaseAPI.main:app", host=API_HOST, port=API_PORT, reload=True)
