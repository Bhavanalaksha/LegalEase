# Phase 4: Project Planning Phase
## Document: Sprint Plan & Milestone Execution Guide

---

### Sprint Cadence & Strategy

The project adopted 1-week iterative sprints designed to ensure rapid prototyping, continuous integration, and frequent testing checkpoints.

---

### 1. Sprint Breakdown

#### Sprint 1: Foundation & Requirements
- **Goal:** Define system scope, select optimal AI model, and formulate architectural contracts.
- **Key Tasks:**
  - Evaluated LLM options: Selected Gemini 1.5 Pro for superior structured legal reasoning.
  - Authored IEEE 830-compliant SRS and use case specifications.
  - Designed system architecture and data flow diagrams.
- **Sprint Retrospective:** Clear Pydantic schemas decided upfront saved significant integration friction between frontend and backend.

#### Sprint 2: Core Engine & AI Development
- **Goal:** Build the document generation engine, text sanitizer, and document formatters.
- **Key Tasks:**
  - Configured `ai_core/gemini_generator.py` with structured prompt engineering.
  - Implemented `ai_core/generator.py` with `python-docx` and `fpdf2` compilers.
  - Created high-res vector branding assets (`Logo.png` and `inverseLogo.png`).
- **Sprint Retrospective:** Embedding custom fallback templates ensured zero downtime even during API quota exhaustion.

#### Sprint 3: API & Web Application Assembly
- **Goal:** Wire the FastAPI REST endpoint and build the Streamlit reactive UI.
- **Key Tasks:**
  - Initialized FastAPI server (`legalEaseAPI/main.py`) with CORS middleware.
  - Built POST `/generate` route handling `DocumentRequest` validation.
  - Designed Streamlit frontend with 3-column logo header, dark preview card, and inline editor.
- **Sprint Retrospective:** Streamlit state management (`st.session_state`) made inline editing seamless.

#### Sprint 4: Verification, Hardening & Academic Submissions
- **Goal:** Verify system stability, achieve 100% test pass rate, and finalize the 8-phase submission portfolio.
- **Key Tasks:**
  - Executed automated Pytest test suite covering endpoints, generators, and sanitizers (10/10 tests passed).
  - Drafted User Manual, Developer Guide, and Swagger API Reference.
  - Scripted and prepared demonstration artifacts and slide deck.
- **Sprint Retrospective:** Project fully verified, documented, and ready for deployment and submission.
