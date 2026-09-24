# Phase 5: Project Development Phase
## Document: Codebase Overview & Implementation Details

---

### 1. Technology Stack Implementation

| Component | Framework / Library | Version | Role in LegalEase |
| :--- | :--- | :--- | :--- |
| **API Backend** | FastAPI | `>=0.110.0` | Asynchronous REST API microservice |
| **ASGI Server** | Uvicorn | `>=0.28.0` | High-concurrency web server |
| **Frontend UI** | Streamlit | `>=1.32.0` | Reactive web interface with session state |
| **AI LLM Core** | google-generativeai | `>=0.4.0` | Google Gemini 1.5 Pro / Flash integration |
| **Word Compiler**| python-docx | `>=1.1.0` | Microsoft Word OpenXML generation & table builder |
| **PDF Compiler** | fpdf2 | `>=2.7.8` | Vector PDF rendering with custom headers/footers |
| **Image Core** | Pillow | `>=10.2.0` | Scalable raster graphics and logo synthesis |
| **Validation** | Pydantic | `>=2.6.0` | Data contract enforcement and schema docs |
| **HTTP Client** | Requests & HTTPX | `>=2.31.0` | Client-server communication & test client |
| **Test Suite** | Pytest | `>=8.0.0` | Automated unit & integration verification |

---

### 2. Key Code Implementations

#### 2.1 Backend Route Handler (`legalEaseAPI/routes.py`)
```python
@router.post("/generate", response_model=DocumentResponse)
def generate_legal_document(request: DocumentRequest):
    try:
        response = gemini_generator.generate_document(
            document_type=request.document_type,
            parties=request.parties,
            terms=request.terms,
            dates=request.dates
        )
        return DocumentResponse(document=response, status="success")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Generation failed: {str(e)}")
```

#### 2.2 Text Sanitizer (`ai_core/generator.py`)
```python
def sanitize_text(text: str) -> str:
    replacements = {
        '“': '"', '”': '"', '‘': "'", '’': "'",
        '—': ' - ', '–': ' - ', '…': '...',
        '\u00a0': ' ', '\t': '    ', '\r\n': '\n'
    }
    sanitized = text
    for orig, rep in replacements.items():
        sanitized = sanitized.replace(orig, rep)
    return sanitized.strip()
```

#### 2.3 Running the Application
To run the full stack:
```cmd
run.bat
```
Or individually:
```cmd
python -m uvicorn legalEaseAPI.main:app --host 0.0.0.0 --port 8000 --reload
python -m streamlit run frontend/app.py
```
