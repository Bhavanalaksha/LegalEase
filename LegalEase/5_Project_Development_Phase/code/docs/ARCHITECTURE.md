# LegalEase System Architecture

## Architecture Diagram

```
+-------------------------------------------------------------+
|                      Streamlit Frontend                     |
|           (Input Capture, Live Preview, Exporter)           |
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

## Core Modules
1. **`ai_core.gemini_generator`**: Google Gemini AI model interface with intelligent offline template fallback.
2. **`ai_core.generator`**: Text sanitizer, Word (.docx) generator with logo and tables, and PDF (.pdf) generator with headers and footers.
3. **`legalEaseAPI.main` & `legalEaseAPI.routes`**: FastAPI application exposing `/generate` and `/`.
4. **`frontend.app.py`**: Streamlit user interface with dark styling and multi-format downloads.
