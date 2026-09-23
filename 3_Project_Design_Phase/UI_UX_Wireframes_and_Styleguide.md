# Phase 3: Project Design Phase
## Document: UI/UX Wireframes, Styleguide & User Flow

---

### 1. Design System & Visual Tokens

| Token | Value / Specification | Usage |
| :--- | :--- | :--- |
| **Primary Background** | `#0f172a` (Deep Slate / Dark Navy) | Full-screen app background |
| **Surface / Card BG** | `#1e293b` (Slate 800) | Containers, input backgrounds, cards |
| **Accent Primary** | `#38bdf8` (Sky Blue) | Focus rings, buttons, section titles |
| **Accent Luxury** | `#d4af37` / `#eab308` (Gold) | Scales of justice logo, highlights |
| **Text Primary** | `#f8fafc` (Pure Slate White) | Headings, labels, generated text |
| **Text Muted** | `#94a3b8` (Slate 400) | Placeholders, captions, footers |
| **Success Alert** | `#10b981` (Emerald Green) | Success toasts and notifications |
| **Document Typography**| `Times New Roman, Times, serif` | Official legal preview and exports |

---

### 2. High-Fidelity ASCII Wireframe

```
+---------------------------------------------------------------------------------+
|                                                                                 |
|                               [   ⚖️ LegalEase   ]                              |
|                         AI Legal Document Generator                             |
|                                                                                 |
|   +-------------------------------------------------------------------------+   |
|   | > [⚡ Quick Fill with Sample Scenarios]                                  |   |
|   +-------------------------------------------------------------------------+   |
|                                                                                 |
|   Document Type (Ex. Agreement, Contract, NDA)                                  |
|   [ Freelance Work Contract                                               ]     |
|                                                                                 |
|   Parties Involved                                                              |
|   [ Jane Doe (Service Provider), TechNova Inc. (Client)                   ]     |
|   [                                                                       ]     |
|                                                                                 |
|   Terms & Conditions (Use semicolons for bullet points)                         |
|   [ Work must be delivered by May 15, 2025;                               ]     |
|   [ Payment will be made within 7 days of invoice;                        ]     |
|   [ The client retains intellectual property rights;                      ]     |
|                                                                                 |
|   Effective Date                                                                |
|   [ April 15, 2025                                                        ]     |
|                                                                                 |
|   [                        🚀 GENERATE DOCUMENT                           ]     |
|                                                                                 |
|   ===========================================================================   |
|   [✅ Document Generated Successfully!                                       ]   |
|                                                                                 |
|   +-------------------------------------------------------------------------+   |
|   |                         OFFICIAL LEGAL PREVIEW                          |   |
|   |                                                                         |   |
|   |  FREELANCE WORK CONTRACT                                                |   |
|   |  This Freelance Work Contract is entered into as of April 15, 2025...   |   |
|   |                                                                         |   |
|   |  BY AND BETWEEN: Jane Doe (Provider) AND TechNova Inc. (Client)...      |   |
|   |  1. SCOPE OF SERVICES: ...                                              |   |
|   +-------------------------------------------------------------------------+   |
|                                                                                 |
|   [ 📝 Click to Edit Document ]                                                 |
|                                                                                 |
|   📥 Download Document                                                          |
|   +--------------------+  +---------------------+  +------------------------+   |
|   |  📄 Download .TXT  |  |  📘 Download .DOCX  |  |   📕 Download .PDF     |   |
|   +--------------------+  +---------------------+  +------------------------+   |
|                                                                                 |
|         LegalEase Inc. © 2026 | Powered by FastAPI & Google Gemini              |
+---------------------------------------------------------------------------------+
```

---

### 3. User Interaction Journey

1. **Discovery:** User opens browser at `http://localhost:8501`.
2. **Template Selection:** User either selects a pre-packaged preset (e.g., NDA or Freelance Contract) or types custom parties and clauses into the form fields.
3. **Trigger Generation:** User presses `Generate Document`. A glowing progress spinner indicates AI generation.
4. **Visual Review:** Within 3 seconds, a dark-themed official preview card renders the formatted legal document with sections and clauses.
5. **Interactive Customization:** If adjustments are required, clicking "Click to Edit Document" enables immediate inline modification.
6. **Multi-Format Export:** The user clicks on `.DOCX` for Word, `.PDF` for print, or `.TXT` for instant copy-pasting.
