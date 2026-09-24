# Phase 5: Project Development Phase
## Document: Architecture & Module Guide

---

### 1. Source Directory Hierarchy

```
LEGALEASE/
├── ai_core/
│   ├── __init__.py
│   ├── gemini_generator.py      # AI Core: Google Gemini 1.5 Pro integration + Offline Engine
│   └── generator.py             # Formatter: docx, pdf, txt compilers, sanitizer, HTML preview
├── frontend/
│   ├── __init__.py
│   └── app.py                   # Presentation: Streamlit responsive web application
├── legalEaseAPI/
│   ├── __init__.py
│   ├── main.py                  # API Server: FastAPI application & CORS initialization
│   └── routes.py                # Router: /generate endpoint & Pydantic request models
├── image/
│   ├── Logo.png                 # Official dark logo emblem for DOCX & PDF exports
│   └── inverseLogo.png          # Light-contrast logo emblem for dark-mode web UI
├── docs/
│   ├── API_DOCUMENTATION.md
│   └── ARCHITECTURE.md
├── config.py                    # Global system configuration and path resolver
├── .env.example                 # Template for API credentials
├── .env                         # Local runtime environment file
├── requirements.txt             # Pinned project dependencies
├── run.bat                      # Windows launcher script
└── run.sh                       # Unix/macOS launcher script
```

---

### 2. Module Specifications

#### 2.1 `ai_core.gemini_generator.py`
- **Class:** `GeminiDocumentGenerator`
- **Primary Function:**
  - `generate_document(document_type: str, parties: str, terms: str, dates: str) -> str`
- **Logic:**
  1. Configures Google Generative AI client with `GEMINI_API_KEY`.
  2. Constructs a structured prompt enforcing title, recitals, numbered covenants, and signature blocks.
  3. If API is offline or key is unconfigured, activates `_generate_fallback_legal_document()`, delivering a complete, customized, valid legal contract.

#### 2.2 `ai_core.generator.py`
- **Functions:**
  - `sanitize_text(text: str) -> str`: Cleans typographic characters, smart quotes, em-dashes, and tab characters.
  - `format_docx(text: str, doc_type: str) -> bytes`: Compiles OpenXML Word `.docx` containing header logo, Times New Roman typography, 1-inch margins, parsed terms table, and legal footer.
  - `format_pdf(text: str, doc_type: str) -> bytes`: Implements `LegalPDF(FPDF)` with centered logo, page dividers, bulleted covenants, and `"LegalEase Inc. | contact@legalease.com | All Rights Reserved."` running footer.
  - `format_html_preview(text: str) -> str`: Transforms markdown into a styled dark-theme HTML card with glowing headings and bullet styling.

#### 2.3 `legalEaseAPI.routes.py`
- **Pydantic Model:** `DocumentRequest`
  - `document_type: str`
  - `parties: str`
  - `terms: str`
  - `dates: str`
- **Endpoint:** `POST /generate`
  - Validates request body, dispatches parameters to `gemini_generator`, and returns JSON `{ "document": "...", "status": "success" }`.

#### 2.4 `frontend.app.py`
- **Framework:** Streamlit
- **Features:**
  - Configures centered layout with custom CSS.
  - Renders 3-column logo banner and header.
  - Quick-Fill scenario dropdown (Freelance Contract, NDA, Lease Agreement, Offer Letter).
  - Validated input fields.
  - Asynchronous progress spinner during AI generation.
  - Official legal preview card.
  - Inline revision editor (`st.text_area`) syncing to session state.
  - 1-click download buttons for `.TXT`, `.DOCX`, and `.PDF`.
