# Phase 4: Project Planning Phase
## Document: Risk Assessment & Mitigation Matrix

---

### 1. Risk Evaluation Matrix

| Risk ID | Risk Description | Probability (1-5) | Impact (1-5) | Risk Score (P x I) | Mitigation Strategy |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **RSK-01** | **Gemini API Rate Limiting / Quota Exhaustion** | 3 | 4 | **12 (Medium)** | Implemented an intelligent standardized offline legal template fallback generator in `ai_core/gemini_generator.py` that activates automatically when API quotas are hit. |
| **RSK-02** | **Invalid Typography / Encoding in PDF Export** | 4 | 3 | **12 (Medium)** | Engineered `sanitize_text()` to normalize smart quotes (`“`, `”`, `’`), em-dashes, and non-breaking spaces into standard ASCII equivalents before passing to FPDF. |
| **RSK-03** | **Malformed User Semicolon Input** | 3 | 2 | **6 (Low)** | Used resilient regex splitting `re.split(r'[;\n]+', terms)` to accept clauses separated by commas, semicolons, or newlines gracefully. |
| **RSK-04** | **Backend Service Connection Drop** | 2 | 4 | **8 (Medium)** | Built seamless fallback in `frontend/app.py` so the UI automatically calls the internal core generator if FastAPI is unavailable. |
| **RSK-05** | **Sensitive Data Leakage** | 2 | 5 | **10 (Medium)** | Designed system to be 100% stateless: no database persistence of private client names, contract terms, or financial amounts. |
| **RSK-06** | **OpenXML / DOCX Layout Corruption** | 1 | 4 | **4 (Low)** | Enforced structured paragraph and table builders with standard 1-inch margins and verified via automated unit testing. |

---

### 2. Contingency Plans
1. **API Key Unavailable during Viva / Evaluation:** The offline engine generates high-quality standard contracts without external internet or API credentials.
2. **Missing Dependencies on Target Machines:** Provided pinned `requirements.txt` and verified compatibility with Python 3.10 through Python 3.14.
