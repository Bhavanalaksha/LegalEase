# Phase 3: Project Design Phase
## Document: System Architecture Document

---

### 1. High-Level Architectural Overview

LegalEase implements a modular, service-oriented multi-tier architecture designed for separation of concerns, high throughput, and developer extensibility.

```mermaid
graph TD
    subgraph Client_Layer ["Client Layer (Frontend)"]
        UI["Streamlit Web UI (app.py)"]
        Form["Input Form Component"]
        Preview["Dark Preview Card (HTML)"]
        Editor["Inline Document Editor"]
        Downloader["Multi-Format Exporter"]
    end

    subgraph API_Layer ["API Layer (FastAPI Backend)"]
        Router["FastAPI Router (routes.py)"]
        Validator["Pydantic Schema Validation"]
        MainApp["Main Server (main.py)"]
    end

    subgraph Core_Layer ["Core Processing & AI Engine"]
        GenAI["Gemini AI Integration (gemini_generator.py)"]
        Fallback["Standardized Legal Engine"]
        Sanitizer["Text Sanitizer Engine"]
        DOCX_Engine["python-docx Compiler"]
        PDF_Engine["fpdf2 Engine"]
    end

    subgraph External_Cloud ["Cloud Services & Storage"]
        GeminiAPI["Google Gemini 1.5 Pro API"]
        Assets["Branding Assets (Logo.png)"]
    end

    UI --> Form
    Form -->|HTTP POST /generate| Router
    Router --> Validator
    Validator --> GenAI
    GenAI -.->|Cloud Prompt| GeminiAPI
    GenAI -.->|Offline Fallback| Fallback
    GenAI --> Sanitizer
    Sanitizer --> Router
    Router -->|JSON Response| UI
    UI --> Preview
    UI --> Editor
    Editor --> Downloader
    Downloader --> DOCX_Engine
    Downloader --> PDF_Engine
    Assets -.-> DOCX_Engine
    Assets -.-> PDF_Engine
```

---

### 2. Tier Breakdown & Responsibilities

#### 2.1 Presentation Tier (Frontend)
- **Technology:** Streamlit 1.32+
- **File:** `frontend/app.py`
- **Role:** Handles user interaction, form inputs, local state (`st.session_state`), live previews, inline revisions, and client downloads.
- **Resilience:** Gracefully falls back to direct internal core generator if backend API is offline during quick local runs.

#### 2.2 Application Tier (Backend API)
- **Technology:** FastAPI 0.110+, Uvicorn ASGI Server
- **Files:** `legalEaseAPI/main.py`, `legalEaseAPI/routes.py`
- **Role:** Exposes `/generate` endpoint, validates schema with Pydantic, performs error handling and logging, and returns normalized JSON responses.

#### 2.3 Core Intelligence & Export Tier
- **Technology:** Google Generative AI SDK, python-docx, fpdf2, Pillow
- **Files:** `ai_core/gemini_generator.py`, `ai_core/generator.py`
- **Role:**
  - `GeminiDocumentGenerator`: Formulates legal prompt, executes AI inference, or invokes the pre-templated legal draft generator.
  - `sanitize_text`: Cleans special characters and typographic quotes.
  - `format_docx`: Compiles Word documents with logo, Times New Roman, terms table, and legal footer.
  - `format_pdf`: Builds high-res PDF with header logo, margins, and legal disclaimer footer.
  - `format_html_preview`: Stylizes document into dark-theme HTML.

---

### 3. Design Patterns Utilized
1. **Model-View-Controller (MVC):** Frontend acts as View/Controller; FastAPI acts as Controller; AI Core acts as Model.
2. **Strategy Pattern:** Generator selects between Google Gemini API strategy and Offline Template strategy based on API key availability.
3. **Builder Pattern:** `format_docx` and `format_pdf` construct complex multi-page documents incrementally from text blocks.
4. **Adapter Pattern:** `sanitize_text` normalizes incompatible string encodings for safe downstream file writing.
