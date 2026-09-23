# Phase 2: Requirement Analysis Phase
## Document: Functional and Non-Functional Requirements

---

### 1. Functional Requirements (FR)

| ID | Requirement Name | Description | Priority |
| :--- | :--- | :--- | :--- |
| **FR-01** | **User Input Capture** | The system shall capture Document Type, Involved Parties, Terms & Conditions (semicolon-separated), and Effective Date. | High (P0) |
| **FR-02** | **Input Validation** | The API backend shall validate incoming payloads using Pydantic schemas, returning HTTP 422 if required fields are missing. | High (P0) |
| **FR-03** | **AI Legal Generation** | The system shall prompt Google Gemini 1.5 Pro to synthesize comprehensive, legally sound documents with standard legal clauses. | High (P0) |
| **FR-04** | **Offline Fallback Engine** | If the Gemini API key is missing or network failure occurs, the engine shall generate a pre-templated legal draft without crashing. | High (P0) |
| **FR-05** | **Text Sanitization** | The system shall sanitize typographic smart quotes, dashes, and whitespace to prevent formatting bugs across export formats. | High (P0) |
| **FR-06** | **Live HTML Preview** | The frontend shall render the generated document in an elegant, scrollable dark-themed HTML preview card. | High (P0) |
| **FR-07** | **Inline Document Revision** | Users shall be able to toggle an edit textarea to customize the generated text prior to file download. | High (P0) |
| **FR-08** | **DOCX Export** | The system shall compile a Microsoft Word `.docx` file featuring embedded logo, Times New Roman typography, terms table, and footer. | High (P0) |
| **FR-09** | **PDF Export** | The system shall compile an A4 `.pdf` file with branded header logo, page numbers, and copyright footer on all pages. | High (P0) |
| **FR-10** | **Plain Text (.TXT) Export** | The system shall allow 1-click download of the raw text document for terminal or email usage. | High (P0) |
| **FR-11** | **Scenario Preset Loader** | The frontend shall provide quick-fill presets for Freelance Contract, NDA, Residential Lease, and Offer Letter. | Medium (P1) |

---

### 2. Non-Functional Requirements (NFR)

#### 2.1 Performance & Latency
- **NFR-P1 (Response Time):** Document generation shall complete in under **10 seconds** under standard network conditions.
- **NFR-P2 (Export Speed):** Compiling DOCX, PDF, and TXT files from memory shall execute in under **500 milliseconds**.
- **NFR-P3 (Memory Consumption):** Memory footprint for the combined frontend and backend services shall remain below **350 MB RAM**.

#### 2.2 Reliability & Availability
- **NFR-R1 (Graceful Degradation):** The frontend shall seamlessly fallback to direct core generation if the FastAPI microservice is offline.
- **NFR-R2 (Uptime):** Backend service shall sustain 99.9% uptime with automated error recovery.

#### 2.3 Usability & Aesthetics
- **NFR-U1 (Modern Aesthetic):** Interface must feature dark mode palette, gold accents, clear typography, and responsive controls.
- **NFR-U2 (Zero Training Curve):** Any user should be able to generate and download a contract in 3 clicks.

#### 2.4 Security & Data Privacy
- **NFR-S1 (Stateless Processing):** Client details and agreements are processed in-memory and not written to long-term database storage, safeguarding private corporate data.
- **NFR-S2 (CORS Protection):** API endpoints configure explicit Cross-Origin Resource Sharing boundaries.
