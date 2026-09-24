# Phase 1: Brainstorming & Ideation Phase
## Document: Ideation & Feature Prioritization Matrix

---

### 1. Ideation Brainstorming Session Log

During the initial brainstorming workshops, the team generated 15 potential product concepts and feature ideas to address the problem statement:

1. **Idea 1: Static Web Form to Fill Hardcoded PDF Templates**
   - *Verdict:* Too rigid. Cannot handle diverse contract variations or custom user terms.
2. **Idea 2: Rule-Based Logic Engine (If/Else Clause Concatenation)**
   - *Verdict:* High maintenance; breaks down when users enter open-ended custom requirements.
3. **Idea 3: Full Generative AI LLM Architecture (Gemini 1.5 Pro)**
   - *Verdict:* Highly flexible, context-aware, understands legal jargon, can formulate natural clauses from user bullet points.
4. **Idea 4: Decoupled RESTful Architecture (FastAPI Backend + Streamlit Frontend)**
   - *Verdict:* Chosen. Excellent separation of concerns, high scalability, and rapid interface responsiveness.
5. **Idea 5: In-Browser Live Markdown/HTML Preview**
   - *Verdict:* Critical for user trust; allows reviewing legal text before exporting.
6. **Idea 6: Inline Document Editor**
   - *Verdict:* Essential so users can tweak specific clauses before final printing.
7. **Idea 7: Triple-Format Export Engine (.TXT, .DOCX, .PDF)**
   - *Verdict:* Industry standard; provides plain text for code/emails, Word for redlining, and branded PDF for signing.
8. **Idea 8: Automatic Summary Terms Table Generation**
   - *Verdict:* Enhances contract readability by extracting key covenants into a clear table.

---

### 2. Feature Prioritization Matrix (Value vs. Complexity)

```
       HIGH VALUE
           ^
           |   [P0: Core LLM Generation]       [P0: Tri-Format Export (.docx/.pdf)]
           |   [P0: REST API Backend]          [P1: Inline Editor]
           |   [P0: Dark UI & Preview]         [P1: Auto Terms Table]
           |
           |   -------------------------------------------------------------------
           |
           |   [P2: Pre-filled Presets]        [P3: Multi-Party E-Signatures]
           |   [P2: Offline Fallback Engine]   [P3: Multi-Language Translation]
           |
           +----------------------------------------------------------------------->
          LOW COMPLEXITY                                            HIGH COMPLEXITY
```

---

### 3. MoSCoW Prioritization Table

| Category | Features Included | Rationale |
| :--- | :--- | :--- |
| **Must Have (P0)** | - Gemini 1.5 Pro prompt engineering engine<br>- FastAPI `/generate` POST endpoint<br>- Streamlit responsive UI<br>- .TXT, .DOCX, and .PDF export engines<br>- Input validation for document type, parties, terms, date | Fundamental requirements mandated by the SmartBridge project specification. |
| **Should Have (P1)** | - Inline document editing textarea<br>- Dark-mode stylized HTML document card<br>- Branded headers, logo embedding, and legal footers<br>- Summary Table of Terms auto-generation | Elevates the product from a basic script to a polished professional SaaS tool. |
| **Could Have (P2)** | - One-click scenario preset templates (NDA, Lease, Offer Letter)<br>- Offline template fallback generator when API key is missing<br>- Text sanitizer for typographic smart quotes | Guarantees reliability during academic grading, viva demonstration, and offline judging. |
| **Won't Have (P3 - Future)** | - Blockchain-based smart contract execution<br>- Real-time docu-sign biometric authentication<br>- Multi-tenant cloud user management | Deferred to Version 2.0 to maintain focus on the core generation engine. |
