# Phase 3: Project Design Phase
## Document: UML Diagrams (Class, Sequence & Component)

---

### 1. UML Class Diagram

```mermaid
classDiagram
    class DocumentRequest {
        +str document_type
        +str parties
        +str terms
        +str dates
    }

    class DocumentResponse {
        +str document
        +str status
    }

    class GeminiDocumentGenerator {
        -str api_key
        -str model_name
        -GenerativeModel model
        -_init_client() void
        +generate_document(doc_type, parties, terms, dates) str
        -_generate_fallback_legal_document(doc_type, parties, terms, dates) str
    }

    class DocumentFormatter {
        <<utility>>
        +sanitize_text(text: str) str
        +format_docx(text: str, doc_type: str) bytes
        +format_pdf(text: str, doc_type: str) bytes
        +format_html_preview(text: str) str
    }

    class LegalPDF {
        +str doc_type
        +str logo_path
        +header() void
        +footer() void
    }

    DocumentRequest --> GeminiDocumentGenerator : processed by
    GeminiDocumentGenerator --> DocumentResponse : outputs
    DocumentFormatter ..> LegalPDF : instantiates
```

---

### 2. UML Sequence Diagram: End-to-End Generation & Export

```mermaid
sequenceDiagram
    autonumber
    actor User as End User
    participant UI as Streamlit UI (app.py)
    participant API as FastAPI Router (routes.py)
    participant Core as GeminiDocumentGenerator
    participant Gemini as Google Gemini AI / Fallback
    participant Formatter as Document Exporter (generator.py)

    User->>UI: Fills form (Doc Type, Parties, Terms, Dates)
    User->>UI: Clicks "Generate Document"
    UI->>API: HTTP POST /generate (JSON payload)
    API->>Core: generate_document(...)
    Core->>Gemini: generate_content(prompt)
    Gemini-->>Core: Raw generated contract text
    Core-->>API: Returns structured legal document
    API-->>UI: HTTP 200 { document, status: "success" }
    UI->>Formatter: format_html_preview(document)
    Formatter-->>UI: Styled HTML
    UI-->>User: Displays official legal preview card

    opt User Customizes Document
        User->>UI: Clicks "Click to Edit Document"
        User->>UI: Types custom clauses in textarea
        UI->>UI: Updates session_state.generated_text
    end

    opt User Downloads DOCX
        User->>UI: Clicks "Download as .DOCX"
        UI->>Formatter: format_docx(text, doc_type)
        Formatter-->>UI: Returns .docx binary stream
        UI-->>User: Downloads {doc_type}.docx
    end

    opt User Downloads PDF
        User->>UI: Clicks "Download as .PDF"
        UI->>Formatter: format_pdf(text, doc_type)
        Formatter-->>UI: Returns .pdf binary stream
        UI-->>User: Downloads {doc_type}.pdf
    end
```

---

### 3. UML Component Diagram

```mermaid
graph LR
    subgraph UI_Component ["Streamlit Presentation Component"]
        InputView["Input View"]
        EditorView["Editor View"]
        PreviewView["Preview View"]
    end

    subgraph Service_Component ["API Microservice Component"]
        MainService["Main Server"]
        RouteHandler["Route Handler"]
        ReqValidator["Schema Validator"]
    end

    subgraph Intelligence_Component ["AI & Processing Component"]
        GeminiAdapter["Gemini Adapter"]
        SanitizerModule["Text Sanitizer"]
        DocxCompiler["DOCX Compiler"]
        PdfCompiler["PDF Compiler"]
    end

    InputView -->|REST/HTTP| MainService
    MainService --> RouteHandler
    RouteHandler --> ReqValidator
    RouteHandler --> GeminiAdapter
    PreviewView --> SanitizerModule
    EditorView --> DocxCompiler
    EditorView --> PdfCompiler
```
