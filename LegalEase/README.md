# ⚖️ LegalEase: AI-Powered Legal Document Generator

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32%2B-FF4B4B.svg)](https://streamlit.io/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-1.5%20Pro-8E75C2.svg)](https://aistudio.google.com/)
[![Tests](https://img.shields.io/badge/Pytest-10%20Passed%20(100%25)-brightgreen.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)]()

> **SmartBridge / SmartInternz Capstone Project**  
> An end-to-end, production-ready Generative AI platform that democratizes the authoring, customization, and multi-format export of legally binding contracts, NDAs, and agreements.

---

## 📌 Executive Summary
**LegalEase** leverages Google's state-of-the-art **Gemini 1.5 Pro** model to simplify legal document generation. Users input basic contract details—such as document type, involved parties, terms and conditions, and effective dates—and instantly receive structured, professional-grade agreements.

The system features:
- **FastAPI Asynchronous Microservice** for scalable backend document processing.
- **Streamlit Dynamic Frontend** with dark-mode aesthetic, live preview, and inline editor.
- **Multi-Format Export Engine** supporting Plain Text (`.txt`), Microsoft Word (`.docx` with embedded logo, Times New Roman, and terms table), and Branded PDF (`.pdf` with vector headers and legal footers).
- **Intelligent Offline Fallback Engine** guaranteeing 100% operational uptime and testing readiness even without an active API key.

---

## 📂 Phase-Wise Project Submission Structure
As instructed by **SmartBridge**, this repository is meticulously organized into the **8 mandatory submission phases**:

| Phase # | Phase Directory | Key Deliverables Included |
| :---: | :--- | :--- |
| **Phase 1** | [`1_Brainstorming_and_Ideation_Phase/`](./1_Brainstorming_and_Ideation_Phase/) | Problem Statement, Empathy Map, Ideation & Prioritization Matrix, Value Proposition Canvas, Feasibility Study. |
| **Phase 2** | [`2_Requirement_Analysis_Phase/`](./2_Requirement_Analysis_Phase/) | Software Requirements Specification (SRS), Functional & Non-Functional Matrix, Use Case Specs, User Stories. |
| **Phase 3** | [`3_Project_Design_Phase/`](./3_Project_Design_Phase/) | System Architecture Document, Data Flow Diagrams (DFD Level 0, 1, 2), UML Diagrams (Class, Sequence, Component), UI/UX Wireframes. |
| **Phase 4** | [`4_Project_Planning_Phase/`](./4_Project_Planning_Phase/) | Work Breakdown Structure (WBS), Project Schedule & Gantt Chart, Sprint Plan, Risk Mitigation Matrix, RACI Matrix. |
| **Phase 5** | [`5_Project_Development_Phase/`](./5_Project_Development_Phase/) | Complete Source Codebase (`ai_core`, `frontend`, `legalEaseAPI`), Architecture & Module Guides, API Endpoints Spec. |
| **Phase 6** | [`6_Project_Testing_Phase/`](./6_Project_Testing_Phase/) | Comprehensive Test Plan, Test Cases Matrix, Test Execution Report, Automated Pytest Suite (`test_api.py`, `test_generator.py`). |
| **Phase 7** | [`7_Project_Documentation_Phase/`](./7_Project_Documentation_Phase/) | End-User Manual, Developer & Installation Setup Guide, REST API Reference Guide, Release Notes. |
| **Phase 8** | [`8_Project_Demonstration_Phase/`](./8_Project_Demonstration_Phase/) | Word-for-Word Voiceover Script (3–5 mins), Presentation Slide Deck, Demonstration Walkthrough, Google Drive Checklist. |

---

## 🏗️ System Architecture

```
+-------------------------------------------------------------+
|                      Streamlit Frontend                     |
|    (Inputs, Live Dark Preview, Inline Editor, Downloads)    |
+------------------------------+------------------------------+
                               | HTTP POST /generate (JSON)
                               v
+-------------------------------------------------------------+
|                     FastAPI Backend API                     |
|            (Validation, Routing, Exception Handling)        |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
|             AI Core Engine & Export Compilers               |
|      (Google Gemini 1.5 Pro, Text Sanitizer, DOCX, PDF)     |
+-------------------------------------------------------------+
```

---

## ⚡ Quick Start Guide

### 1. Clone & Setup
```bash
git clone https://github.com/Bhavanalaksha/LegalEase.git
cd LegalEase
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate # Linux/macOS
pip install -r requirements.txt
```

### 2. Environment Configuration (Optional)
Copy `.env.example` to `.env` and add your Google Gemini API key:
```env
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-1.5-pro
API_HOST=0.0.0.0
API_PORT=8000
API_BASE_URL=http://localhost:8000
```
*(Note: If you leave `GEMINI_API_KEY` empty, LegalEase automatically uses its built-in offline legal template generator).*

### 3. Run the Application
**On Windows:**
Double click `run.bat` or run:
```cmd
run.bat
```

**Manual Start:**
- **Terminal 1 (Backend API):**
  ```cmd
  python -m uvicorn legalEaseAPI.main:app --host 0.0.0.0 --port 8000 --reload
  ```
- **Terminal 2 (Frontend UI):**
  ```cmd
  python -m streamlit run frontend/app.py
  ```

Open your browser at **`http://localhost:8501`**.

---

## 🧪 Automated Testing
Run the complete automated test suite (10 unit & integration tests):
```cmd
python -m pytest 6_Project_Testing_Phase/tests/ -v
```
**Results:** `10 passed in <1s (100% pass rate)`

---

## 🎥 Demonstration Video & Google Drive Submission
Refer to [`8_Project_Demonstration_Phase/Demo_Video_Recording_Script.md`](./8_Project_Demonstration_Phase/Demo_Video_Recording_Script.md) for the exact word-for-word voiceover script covering:
1. Project Name & Overview
2. Purpose of the Project
3. Benefits & Real-World Use
4. Live System Execution & Inline Customization
5. Final Multi-Format Export (.txt, .docx, .pdf)

---

## 👥 Authors & Team
- **Team LegalEase**
- Capstone Project in partnership with **SmartBridge & SmartInternz**
- Faculty Advisor: Department of Computer Science & Engineering
