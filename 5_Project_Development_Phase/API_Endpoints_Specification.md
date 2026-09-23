# Phase 5: Project Development Phase
## Document: API Endpoints Specification

---

### 1. Base URL
- **Local:** `http://localhost:8000`
- **Swagger UI Interactive Docs:** `http://localhost:8000/docs`
- **ReDoc Interactive Docs:** `http://localhost:8000/redoc`

---

### 2. Endpoints Catalog

#### 2.1 Root Health Check
- **Path:** `/`
- **Method:** `GET`
- **Description:** Verifies service availability and reports server status.
- **Request Parameters:** None
- **Response (200 OK):**
```json
{
  "message": "Welcome to LegalEase AI Legal Document Generator API",
  "status": "online",
  "version": "1.0.0",
  "documentation": "/docs"
}
```

---

#### 2.2 Generate Legal Document
- **Path:** `/generate`
- **Method:** `POST`
- **Content-Type:** `application/json`
- **Description:** Accepts contract specifications, invokes the Gemini AI Core, and returns a formatted legal agreement.
- **Request Body:**
```json
{
  "document_type": "Freelance Work Contract",
  "parties": "Jane Doe (Service Provider), TechNova Inc. (Client)",
  "terms": "Work must be delivered by May 15, 2025; Payment will be made within 7 days of invoice; The client retains intellectual property rights; Confidentiality must be maintained at all times;",
  "dates": "April 15, 2025"
}
```
- **Response (200 OK):**
```json
{
  "document": "## FREELANCE WORK CONTRACT\n\nThis Freelance Work Contract (the \"Agreement\") is entered into and made effective as of April 15, 2025...\n\nBY AND BETWEEN:\nJane Doe (Service Provider)...\nAND:\nTechNova Inc. (Client)...\n\n1. PURPOSE AND SCOPE OF WORK...",
  "status": "success"
}
```
- **Error Responses:**
  - `422 Unprocessable Entity`: Missing or malformed required fields.
  - `500 Internal Server Error`: AI inference failure or unexpected backend exception.
