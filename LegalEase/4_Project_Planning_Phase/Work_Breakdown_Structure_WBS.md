# Phase 4: Project Planning Phase
## Document: Work Breakdown Structure (WBS)

---

### Hierarchical Work Breakdown Structure

```
1.0 LegalEase Project
├── 1.1 Project Initiation & Ideation
│   ├── 1.1.1 Problem Statement Formulation
│   ├── 1.1.2 Stakeholder Empathy Mapping
│   ├── 1.1.3 Value Proposition Definition
│   └── 1.1.4 Feasibility & Model Selection Analysis
├── 1.2 Requirements Engineering
│   ├── 1.2.1 Stakeholder User Persona Definition
│   ├── 1.2.2 Functional Requirements Matrix (FR-01 to FR-11)
│   ├── 1.2.3 Non-Functional Requirements Specification
│   └── 1.2.4 Formal IEEE 830-style SRS Documentation
├── 1.3 System Architecture & UI/UX Design
│   ├── 1.3.1 Service-Oriented Architecture Design
│   ├── 1.3.2 Data Flow Modeling (Level 0, 1, 2)
│   ├── 1.3.3 UML Modeling (Class, Sequence, Component)
│   └── 1.3.4 Brand Design (Scales of Justice Logo & Tokens)
├── 1.4 Core Development & AI Integration
│   ├── 1.4.1 Google Gemini 1.5 Pro AI Adapter Setup
│   ├── 1.4.2 Standardized Legal Fallback Engine Implementation
│   ├── 1.4.3 Multi-Format Exporter (.DOCX with Tables & .PDF with Headers)
│   ├── 1.4.4 FastAPI RESTful Server Implementation (/generate)
│   └── 1.4.5 Streamlit Web UI & Inline Editor Development
├── 1.5 Quality Assurance & Verification
│   ├── 1.5.1 Test Plan & Test Case Matrix Authoring
│   ├── 1.5.2 Unit Testing (Text Sanitizer & Exporters)
│   ├── 1.5.3 Integration Testing (FastAPI TestClient)
│   └── 1.5.4 Automated Pytest Suite Execution
├── 1.6 Project Documentation
│   ├── 1.6.1 End-User Manual & Step-by-Step Guide
│   ├── 1.6.2 Developer & Installation Setup Guide
│   ├── 1.6.3 REST API Reference Guide (Swagger/OpenAPI)
│   └── 1.6.4 Version 1.0 Release Notes
└── 1.7 Project Demonstration & Submission
    ├── 1.7.1 Timed Voiceover Demo Video Script
    ├── 1.7.2 Pitch Presentation Slide Deck
    ├── 1.7.3 Execution Walkthrough Guide
    └── 1.7.4 GitHub Public Repository Finalization
```

---

### WBS Dictionary Sample

| Work Package ID | Work Package Title | Deliverables | Assigned Role |
| :--- | :--- | :--- | :--- |
| **1.4.1** | Gemini AI Adapter | `ai_core/gemini_generator.py` | AI Engineer |
| **1.4.3** | Multi-Format Exporter | `ai_core/generator.py` (docx, pdf) | Backend Engineer |
| **1.4.4** | FastAPI Backend | `legalEaseAPI/main.py`, `routes.py` | Backend Engineer |
| **1.4.5** | Streamlit UI | `frontend/app.py` | Frontend Engineer |
| **1.5.4** | Pytest Automation | `6_Project_Testing_Phase/tests/` | QA Engineer |
| **1.7.1** | Video Voiceover Script| `Demo_Video_Recording_Script.md`| Team Lead / Presenter |
