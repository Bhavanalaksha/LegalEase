#!/usr/bin/env bash
echo "========================================================"
echo "       Starting LegalEase AI Document Generator"
echo "========================================================"

# Start FastAPI in background
echo "[1/2] Starting FastAPI Backend on http://localhost:8000 ..."
python -m uvicorn legalEaseAPI.main:app --host 0.0.0.0 --port 8000 --reload &
API_PID=$!

sleep 2

# Start Streamlit in foreground
echo "[2/2] Starting Streamlit Frontend on http://localhost:8501 ..."
python -m streamlit run frontend/app.py

kill $API_PID
