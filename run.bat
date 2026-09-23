@echo off
echo ========================================================
echo        Starting LegalEase AI Document Generator
echo ========================================================

echo [1/2] Starting FastAPI Backend on http://localhost:8000 ...
start "LegalEase Backend API" cmd /k "python -m uvicorn legalEaseAPI.main:app --host 0.0.0.0 --port 8000 --reload"

timeout /t 2 >nul

echo [2/2] Starting Streamlit Frontend on http://localhost:8501 ...
start "LegalEase Streamlit UI" cmd /k "python -m streamlit run frontend/app.py"

echo ========================================================
echo LegalEase services initiated!
echo Backend API Docs: http://localhost:8000/docs
echo Frontend Web UI : http://localhost:8501
echo ========================================================
