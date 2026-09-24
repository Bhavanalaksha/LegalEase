import os
import re
from typing import Optional
from config import GEMINI_API_KEY, GEMINI_MODEL

class GeminiDocumentGenerator:
    """
    Generates formal legal documents using Google's Gemini Generative AI model
    with an intelligent fallback template engine for offline or unconfigured environments.
    """
    def __init__(self, api_key: Optional[str] = None, model_name: Optional[str] = None):
        self.api_key = api_key or GEMINI_API_KEY or os.getenv("GEMINI_API_KEY", "")
        self.model_name = model_name or GEMINI_MODEL or os.getenv("GEMINI_MODEL", "gemini-1.5-pro")
        self.model = None
        self._init_client()

    def _init_client(self):
        if self.api_key and self.api_key != "your_gemini_api_key_here":
            try:
                import google.generativeai as genai
                genai.configure(api_key=self.api_key)
                self.model = genai.GenerativeModel(self.model_name)
            except Exception as e:
                print(f"[Warning] Failed to initialize Gemini API client: {e}. Fallback engine will be active.")
                self.model = None
        else:
            self.model = None

    def generate_document(self, document_type: str, parties: str, terms: str, dates: str) -> str:
        """
        Generate a comprehensive, legally structured document based on user inputs.
        """
        prompt = (
            f"Generate a comprehensive, professional, and legally sound legal document titled '{document_type}'.\n"
            f"Involved parties: {parties}\n"
            f"Effective Date: {dates}\n"
            f"Terms and conditions:\n{terms}\n\n"
            "Requirements:\n"
            "1. Ensure formal legal structure with numbered sections and standard legal clauses.\n"
            "2. Include Title, Preamble, WHEREAS clauses (Recitals), NOW THEREFORE agreement statement.\n"
            "3. Seamlessly incorporate the provided terms and conditions as numbered clauses or bulleted provisions.\n"
            "4. Include standard clauses for Confidentiality, Governing Law, Severability, and Entire Agreement.\n"
            "5. Include signature and execution blocks at the end for all involved parties.\n"
            "6. Output clear Markdown formatting with headers (##, ###) and clean paragraphs."
        )

        if self.model:
            try:
                response = self.model.generate_content(prompt)
                if response and hasattr(response, "text") and response.text:
                    return response.text.strip()
            except Exception as e:
                print(f"[AI Generator] Gemini API call error: {e}. Falling back to internal legal engine.")

        # Fallback high-quality template generator
        return self._generate_fallback_legal_document(document_type, parties, terms, dates)

    def _generate_fallback_legal_document(self, document_type: str, parties: str, terms: str, dates: str) -> str:
        """
        Generates a pristine, standardized legal document when API is unavailable.
        """
        # Parse parties
        party_list = [p.strip() for p in re.split(r'[,;\n]+', parties) if p.strip()]
        party1 = party_list[0] if len(party_list) > 0 else "First Party"
        party2 = party_list[1] if len(party_list) > 1 else "Second Party"
        
        # Parse terms
        term_items = [t.strip().rstrip(";") for t in re.split(r'[;\n]+', terms) if t.strip()]
        if not term_items:
            term_items = [
                "The parties agree to perform their respective obligations with reasonable diligence.",
                "Payment shall be remitted in full within thirty (30) days of invoice issuance.",
                "Confidential information disclosed hereunder shall remain strictly confidential."
            ]

        terms_formatted = "\n".join([f"- **Clause {i+1}**: {item}" for i, item in enumerate(term_items)])

        doc = f"""## {document_type.upper()}

This **{document_type}** (the "Agreement") is entered into and made effective as of **{dates}** (the "Effective Date"),

### BY AND BETWEEN:

**{party1}** (hereinafter referred to as the "First Party"),

### AND:

**{party2}** (hereinafter referred to as the "Second Party").

---

### RECITALS (WITNESSETH):

WHEREAS, the First Party and the Second Party desire to enter into an arrangement defined by this {document_type}; and

WHEREAS, each party possesses the legal authority, operational competence, and necessary resources to fulfill the commitments described herein;

NOW, THEREFORE, in consideration of the mutual covenants, terms, conditions, and valuable considerations set forth herein, the receipt and sufficiency of which are hereby acknowledged, the parties agree as follows:

---

### 1. PURPOSE AND SCOPE OF WORK
1.1 The purpose of this Agreement is to establish the explicit contractual terms governing the relationship between {party1} and {party2}.
1.2 The parties agree to collaborate faithfully to achieve the objectives outlined in this Agreement and adhere to standard professional ethics and statutory standards.

### 2. SPECIFIC TERMS & CONDITIONS
The parties explicitly covenant, warrant, and agree to the following operational terms:
{terms_formatted}

### 3. TERM AND TERMINATION
3.1 This Agreement shall commence on the **Effective Date ({dates})** and shall continue in full force and effect until satisfied by performance or terminated in writing.
3.2 Either party may terminate this Agreement upon thirty (30) business days written notice to the other party.
3.3 Immediate termination may occur in the event of an uncured material breach following ten (10) days notice.

### 4. CONFIDENTIALITY & PROPRIETARY RIGHTS
4.1 The parties agree to hold in strict confidence all proprietary data, business secrets, and strategic materials disclosed under this Agreement.
4.2 Neither party shall disclose Confidential Information to any third party without prior written authorization.

### 5. GOVERNING LAW AND DISPUTE RESOLUTION
5.1 This Agreement shall be governed by, and construed in accordance with, the laws of the applicable commercial jurisdiction.
5.2 Any dispute arising out of or related to this Agreement shall first be resolved through good-faith mediation before initiating formal arbitration or judicial proceedings.

### 6. SEVERABILITY AND ENTIRE AGREEMENT
6.1 If any provision of this Agreement is held to be invalid or unenforceable, such determination shall not affect the validity of the remaining provisions.
6.2 This Agreement constitutes the entire agreement between the parties concerning the subject matter hereof and supersedes all prior proposals, negotiations, and understandings.

---

### IN WITNESS WHEREOF
The parties hereto have executed this **{document_type}** as of the Effective Date written above.

**FOR {party1.upper()}:**

_____________________________________  
Authorized Signature  
Name: {party1}  
Date: {dates}  


**FOR {party2.upper()}:**

_____________________________________  
Authorized Signature  
Name: {party2}  
Date: {dates}  
"""
        return doc.strip()
