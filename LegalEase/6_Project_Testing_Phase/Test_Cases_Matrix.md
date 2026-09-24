# Phase 6: Project Testing Phase
## Document: Test Cases Matrix

---

### Test Suite Execution Matrix

| Test Case ID | Test Category | Target Component | Test Scenario / Objective | Expected Result | Status |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **TC-01** | Integration | `legalEaseAPI.main` | Health check endpoint `GET /` | Returns HTTP 200 with status `"online"` and API message | **PASSED** |
| **TC-02** | Integration | `legalEaseAPI.routes` | Valid contract generation `POST /generate` | Returns HTTP 200 with non-empty `"document"` and status `"success"` | **PASSED** |
| **TC-03** | Validation | `legalEaseAPI.routes` | Omit required field (`parties`) `POST /generate` | Returns HTTP 422 Unprocessable Entity | **PASSED** |
| **TC-04** | Unit | `ai_core.gemini_generator` | Core generation with parties, terms, date | Contains parties, document title, and effective date in output | **PASSED** |
| **TC-05** | Unit | `ai_core.generator` | DOCX file compilation via `format_docx()` | Returns non-empty bytes starting with zip PK header `PK\x03\x04` | **PASSED** |
| **TC-06** | Unit | `ai_core.generator` | PDF file compilation via `format_pdf()` | Returns non-empty bytes starting with `%PDF` header | **PASSED** |
| **TC-07** | Unit | `ai_core.generator` | Styled HTML generation `format_html_preview()` | Returns HTML string containing `<h3`, `OFFICIAL LEGAL PREVIEW` | **PASSED** |
| **TC-08** | Unit | `ai_core.generator` | Text sanitizer with smart typographic quotes | Replaces curly quotes `“` `”` with straight quotes `"` | **PASSED** |
| **TC-09** | Unit | `ai_core.generator` | Text sanitizer with em-dashes and `\u00a0` | Replaces em-dash with ` - ` and strips non-breaking spaces | **PASSED** |
| **TC-10** | Boundary | `ai_core.generator` | Text sanitizer with empty or null string | Safely returns empty string `""` without crashing | **PASSED** |

---

### Manual Verification Checklist

| Scenario | Input Data | Verification Checkpoints | Result |
| :--- | :--- | :--- | :---: |
| **Freelance Work Contract** | Jane Doe & TechNova Inc. | Document title, 4 clauses, payment term table, execution blocks | **PASSED** |
| **Non-Disclosure Agreement (NDA)** | Disclosing & Receiving Party | 3-year term, confidentiality obligations, return of materials | **PASSED** |
| **Residential Lease** | Landlord & Tenant | Monthly rent, deposit terms, notice period, inspection clause | **PASSED** |
| **Inline Editing** | Modifying contract clauses in textarea | Export files reflect user edits immediately | **PASSED** |
| **DOCX Header & Footer** | Downloaded `.docx` | Centered logo on page 1, running footer on all pages | **PASSED** |
| **PDF Header & Footer** | Downloaded `.pdf` | Header logo, clean borders, copyright footer on all pages | **PASSED** |
