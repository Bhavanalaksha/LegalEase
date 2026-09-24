# LegalEase API Documentation

This directory provides the technical API reference for the LegalEase FastAPI backend service.

## Base URL
- Local: `http://localhost:8000`
- Interactive OpenAPI Swagger: `http://localhost:8000/docs`
- Redoc Interactive Documentation: `http://localhost:8000/redoc`

## Endpoints

### 1. Health Status
- **Method:** `GET /`
- **Summary:** Verify service uptime
- **Response:**
```json
{
  "message": "Welcome to LegalEase AI Legal Document Generator API",
  "status": "online",
  "version": "1.0.0",
  "documentation": "/docs"
}
```

### 2. Generate Legal Document
- **Method:** `POST /generate`
- **Request Body:**
```json
{
  "document_type": "Freelance Work Contract",
  "parties": "Jane Doe (Service Provider), TechNova Inc. (Client)",
  "terms": "Work must be delivered by May 15, 2025; Payment within 7 days of invoice; Client retains IP rights; Confidentiality maintained at all times;",
  "dates": "April 15, 2025"
}
```
- **Response:**
```json
{
  "document": "## FREELANCE WORK CONTRACT\n...",
  "status": "success"
}
```
