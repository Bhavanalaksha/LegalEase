# Phase 3: Project Design Phase
## Document: Data Flow Diagrams (DFD)

---

### 1. Level 0 DFD: Context Diagram

The Context Diagram defines the system boundary for LegalEase and its interactions with external entities (User, Google Gemini Cloud).

```
                      +---------------------------------------+
                      |               End User                |
                      +---------------------------------------+
                             |                         ^
            1. Document Data |                         | 5. Downloaded
               (Type, Party, |                         |    Files (.docx,
               Terms, Date)  |                         |    .pdf, .txt)
                             v                         |
                      +---------------------------------------+
                      |                                       |
                      |          0.0 LegalEase System         |
                      |                                       |
                      +---------------------------------------+
                             |                         ^
            2. Structured    |                         | 3. Raw AI
               Legal Prompt  |                         |    Contract Text
                             v                         |
                      +---------------------------------------+
                      |         Google Gemini AI API          |
                      +---------------------------------------+
```

---

### 2. Level 1 DFD: System Process Flow

The Level 1 DFD breaks down LegalEase into major subprocesses:

```
+----------+      1. Form Input      +-----------------------+
|   User   | ----------------------> | 1.0 Input Capture &   |
|          |                         |     Form Validation   |
+----------+                         +-----------------------+
                                                 |
                                                 | 2. Validated Payload
                                                 v
                                     +-----------------------+
                                     | 2.0 Document Synthesizer| <---> [Google Gemini /
                                     |     (Gemini AI Core)  |        Fallback Store]
                                     +-----------------------+
                                                 |
                                                 | 3. Generated Raw Text
                                                 v
                                     +-----------------------+
                                     | 3.0 Text Sanitizer &  |
                                     |     HTML Formatter    |
                                     +-----------------------+
                                                 |
                                                 | 4. Sanitized Legal Draft
                                                 v
+----------+   5. Interactive Edit   +-----------------------+
|   User   | <---------------------> | 4.0 Preview & Inline  |
+----------+                         |     Editing Engine    |
                                     +-----------------------+
                                                 |
                                                 | 6. Finalized Text Stream
                                                 v
+----------+   7. Deliver Binary     +-----------------------+
|   User   | <---------------------- | 5.0 Document Compiler | <--- [Logo Assets]
+----------+                         |     (DOCX, PDF, TXT)  |
                                     +-----------------------+
```

---

### 3. Level 2 DFD: Detailed Subprocess of Document Compiler (Process 5.0)

```
                       5.0 Document Compiler
                                 |
        +------------------------+------------------------+
        |                                                 |
        v                                                 v
5.1 DOCX Formatting Engine                       5.2 PDF Formatting Engine
 - Set 1-inch margins                             - Initialize A4 portrait
 - Embed header Logo.png                          - Draw centered logo emblem
 - Style Times New Roman 12pt                     - Render divider rule
 - Parse terms into table rows                    - Format section headers
 - Inject execution signatures                    - Add page numbers & footer
 - Stream OpenXML .docx bytes                     - Stream binary .pdf bytes
```
