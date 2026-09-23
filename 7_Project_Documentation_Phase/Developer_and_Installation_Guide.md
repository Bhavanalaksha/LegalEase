# Phase 7: Project Documentation Phase
## Document: Developer & Installation Setup Guide

---

### 1. Prerequisites
- **Python:** Version 3.10, 3.11, 3.12, 3.13, or 3.14+
- **Package Manager:** `pip`
- **Git:** Installed on local machine
- **Google Gemini API Key:** (Optional) Obtain from [Google AI Studio](https://aistudio.google.com/)

---

### 2. Installation Steps

#### Step 2.1: Clone the Repository
```bash
git clone https://github.com/<your-username>/LegalEase.git
cd LegalEase
```

#### Step 2.2: Create and Activate Virtual Environment (Recommended)
On Windows:
```cmd
python -m venv venv
venv\Scripts\activate
```
On Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Step 2.3: Install Dependencies
```bash
pip install -r requirements.txt
```

#### Step 2.4: Configure Environment Variables
Copy `.env.example` to `.env`:
```cmd
copy .env.example .env
```
Open `.env` in an editor and insert your Gemini API key:
```env
GEMINI_API_KEY=AIzaSy...
GEMINI_MODEL=gemini-1.5-pro
API_HOST=0.0.0.0
API_PORT=8000
API_BASE_URL=http://localhost:8000
```
*(Note: If you leave `GEMINI_API_KEY` blank, LegalEase will automatically use its robust standardized offline fallback engine).*

---

### 3. Running the Application

#### Option A: One-Click Windows Launcher
Double-click `run.bat` or run:
```cmd
run.bat
```

#### Option B: Terminal Commands
Terminal 1 (Backend API):
```cmd
python -m uvicorn legalEaseAPI.main:app --host 0.0.0.0 --port 8000 --reload
```
Terminal 2 (Frontend UI):
```cmd
python -m streamlit run frontend/app.py
```

---

### 4. Running the Automated Test Suite
To execute all 10 automated test cases:
```cmd
python -m pytest 6_Project_Testing_Phase/tests/ -v
```
All tests should pass in under 2 seconds.
