# Phase 2: Requirement Analysis Phase
## Document: Use Case Specifications

---

### Use Case Diagram Overview

```
                      +-----------------------------------+
                      |             LegalEase             |
                      +-----------------------------------+
                      |                                   |
                      |  [UC-01: Select / Input Doc Data] |
                      |                 ^                 |
                      |                 | includes        |
    +--------------+  |  [UC-02: Trigger AI Generation]   |  +--------------------+
    |              |  |                 |                 |  |                    |
    |   End User   |->|  [UC-03: Preview Document (HTML)] |  |   Google Gemini    |
    | (Freelancer/ |  |                 |                 |  |      AI Core       |
    |  Founder)    |  |  [UC-04: Edit / Customize Text]   |  |                    |
    |              |  |                 |                 |  +--------------------+
    +--------------+  |  [UC-05: Export Multi-Format]     |            ^
                      |         /       |       \         |            |
                      |      .TXT     .DOCX     .PDF      |------------+
                      +-----------------------------------+
```

---

### Detailed Use Case Specifications

#### UC-01: Generate Legal Document
- **Actor:** End User
- **Pre-conditions:** Web application is loaded in browser.
- **Main Flow:**
  1. User enters document type (e.g., "Freelance Work Contract").
  2. User specifies parties (e.g., "Jane Doe (Provider), TechNova Inc. (Client)").
  3. User enters specific terms separated by semicolons.
  4. User enters effective date (e.g., "April 15, 2025").
  5. User clicks "🚀 Generate Document".
  6. Frontend validates inputs and dispatches HTTP POST payload to `/generate`.
  7. Gemini AI processes prompt and returns structured legal contract.
  8. System renders formatted preview card and displays success confirmation.
- **Post-conditions:** Generated document is stored in session state, ready for editing or export.

#### UC-02: Inline Document Editing
- **Actor:** End User
- **Pre-conditions:** Document has been generated (UC-01 completed).
- **Main Flow:**
  1. User clicks "📝 Click to Edit Document".
  2. System expands full-height interactive textarea populated with the generated text.
  3. User modifies specific wording, adds custom clauses, or edits dates.
  4. Modifications immediately sync with session state.
- **Post-conditions:** Downstream export buttons reflect the edited text.

#### UC-03: Export to Microsoft Word (.DOCX)
- **Actor:** End User
- **Main Flow:**
  1. User clicks "📘 Download as .DOCX".
  2. System streams sanitized text into `format_docx()` generator.
  3. Engine applies Times New Roman font, embeds centered high-resolution logo, constructs terms table, and attaches legal footer.
  4. Browser prompts user to save `{doc_type}.docx`.
- **Post-conditions:** Valid Word file saved to local machine.

#### UC-04: Export to Branded PDF (.PDF)
- **Actor:** End User
- **Main Flow:**
  1. User clicks "📕 Download as .PDF".
  2. System streams text into `format_pdf()` generator.
  3. FPDF engine constructs multi-page layout with centered logo header and running copyright footer.
  4. Browser downloads `{doc_type}.pdf`.
- **Post-conditions:** Formatted PDF document ready for printing or digital signing.
