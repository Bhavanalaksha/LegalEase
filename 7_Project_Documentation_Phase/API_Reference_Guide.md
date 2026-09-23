# Phase 7: Project Documentation Phase
## Document: REST API Reference Guide

---

### 1. Overview
The LegalEase API is built using FastAPI and conforms to OpenAPI 3.1 specifications. It is designed to be consumed by the Streamlit frontend, third-party microservices, mobile apps, or enterprise integrations.

---

### 2. Endpoints Reference

#### 2.1 Health Check & API Status
- **Method:** `GET`
- **Path:** `/`
- **Description:** Verifies service uptime.
- **Request Headers:** None
- **Response Body:**
```json
{
  "message": "Welcome to LegalEase AI Legal Document Generator API",
  "status": "online",
  "version": "1.0.0",
  "documentation": "/docs"
}
```
- **Response Code:** `200 OK`

---

#### 2.2 Document Generation
- **Method:** `POST`
- **Path:** `/generate`
- **Description:** Synthesizes a formal legal agreement from structured parameters.
- **Request Headers:** `Content-Type: application/json`
- **Request Schema (`DocumentRequest`):**

| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| `document_type` | `string` | **Yes** | Formal title or type (e.g., "Freelance Work Contract", "NDA"). |
| `parties` | `string` | **Yes** | Identity and designations of all parties involved. |
| `terms` | `string` | **Yes** | Semicolon-separated obligations, covenants, or terms. |
| `dates` | `string` | **Yes** | Legal effective/commencement date. |

- **Sample Request Body:**
```json
{
  "document_type": "Non-Disclosure Agreement",
  "parties": "Tech Corp (Disclosing), Jane Doe (Receiving)",
  "terms": "Confidentiality maintained for 2 years; Non-disclosure of proprietary algorithms;",
  "dates": "May 1, 2025"
}
```

- **Sample Response Body (`DocumentResponse`):**
```json
{
  "document": "## NON-DISCLOSURE AGREEMENT\n\nThis Non-Disclosure Agreement...",
  "status": "success"
}
```
- **Response Codes:**
  - `200 OK`: Successful document synthesis.
  - `422 Unprocessable Entity`: Validation error (missing required fields).
  - `500 Internal Server Error`: Processing or server exception.
