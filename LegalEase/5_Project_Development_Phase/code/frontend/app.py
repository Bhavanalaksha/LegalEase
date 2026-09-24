import sys
import os
from pathlib import Path

# Add project root to sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

import streamlit as st
import requests
from config import API_BASE_URL, WEB_LOGO_PATH, LOGO_PATH
from ai_core.generator import sanitize_text, format_docx, format_pdf, format_html_preview
from ai_core.gemini_generator import GeminiDocumentGenerator

# Page Configuration
st.set_page_config(
    page_title="LegalEase - AI Legal Document Generator",
    page_icon="⚖️",
    layout="centered"
)

# Custom Styling for Sleek Dark / Contrast Interface
st.markdown("""
<style>
    /* Global styling */
    .main {
        max-width: 850px;
        margin: 0 auto;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        color: #f8fafc;
        border: 1px solid #334155;
        border-radius: 8px;
        padding: 0.6rem 1rem;
        font-weight: 600;
        transition: all 0.2s ease;
    }
    .stButton>button:hover {
        border-color: #38bdf8;
        color: #38bdf8;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(56, 189, 248, 0.15);
    }
    .stDownloadButton>button {
        width: 100%;
        border-radius: 6px;
        font-weight: 500;
    }
    .preset-chip {
        display: inline-block;
        background: #1e293b;
        color: #94a3b8;
        border: 1px solid #334155;
        border-radius: 16px;
        padding: 4px 12px;
        font-size: 12px;
        margin-right: 6px;
        margin-bottom: 6px;
        cursor: pointer;
    }
</style>
""", unsafe_allow_html=True)

# Session State Initialization
if "generated_text" not in st.session_state:
    st.session_state.generated_text = ""
if "show_edit" not in st.session_state:
    st.session_state.show_edit = False

# Three-column layout to center-align the company logo
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if WEB_LOGO_PATH and os.path.exists(WEB_LOGO_PATH):
        st.image(str(WEB_LOGO_PATH), use_container_width=True)
    elif LOGO_PATH and os.path.exists(LOGO_PATH):
        st.image(str(LOGO_PATH), use_container_width=True)
    else:
        st.markdown("<h1 style='text-align: center;'>⚖️ LegalEase</h1>", unsafe_allow_html=True)

# Header and Title
st.markdown("<h2 style='text-align: center; margin-top: -10px; margin-bottom: 25px; color: #f8fafc;'>AI Legal Document Generator</h2>", unsafe_allow_html=True)

# Preset Templates Quick-fill selector
presets = {
    "Freelance Work Contract": {
        "parties": "Jane Doe (Service Provider), TechNova Inc. (Client)",
        "terms": "Work must be delivered by May 15, 2025;\nPayment will be made within 7 days of invoice;\nThe client retains intellectual property rights;\nConfidentiality must be maintained at all times;",
        "dates": "April 15, 2025"
    },
    "Non-Disclosure Agreement (NDA)": {
        "parties": "Alice Smith (Disclosing Party), Quantum Innovations LLC (Receiving Party)",
        "terms": "Recipient agrees to hold proprietary source code and client lists in strict confidence;\nTerm of confidentiality shall endure for a period of three (3) years;\nInformation disclosed in written or oral form marked Confidential is protected;\nEither party may request return or destruction of materials upon termination;",
        "dates": "May 1, 2025"
    },
    "Residential Lease Agreement": {
        "parties": "XYZ Realty Group (Landlord), Johnathan Davis (Tenant)",
        "terms": "Monthly rent shall be $2,200 due on the first day of each calendar month;\nSecurity deposit of $2,200 payable upon execution;\nTenant shall not sub-let the premises without prior written consent;\nLandlord shall provide 24-hour notice prior to non-emergency inspections;",
        "dates": "June 1, 2025"
    },
    "Employment Offer Letter": {
        "parties": "Apex Technologies Corp. (Employer), Sarah Jenkins (Employee)",
        "terms": "Position offered is Senior Software Architect at an annual base salary of $145,000;\nStandard 15 days of paid annual leave plus medical insurance coverage;\nEmployment is at-will subject to a 90-day probationary review;\nEmployee shall execute standard IP assignment and non-solicitation covenants;",
        "dates": "July 15, 2025"
    }
}

with st.expander("⚡ Quick Fill with Sample Scenarios", expanded=False):
    selected_preset = st.selectbox("Choose a scenario template:", list(presets.keys()))
    if st.button("Apply Template Values"):
        data = presets[selected_preset]
        st.session_state["def_type"] = selected_preset
        st.session_state["def_parties"] = data["parties"]
        st.session_state["def_terms"] = data["terms"]
        st.session_state["def_dates"] = data["dates"]
        st.rerun()

# Default Values
default_doc_type = st.session_state.get("def_type", "Freelance Work Contract")
default_parties = st.session_state.get("def_parties", "Jane Doe (Service Provider), TechNova Inc. (Client)")
default_terms = st.session_state.get("def_terms", "Work must be delivered by May 15, 2025;\nPayment will be made within 7 days of invoice;\nThe client retains intellectual property rights;\nConfidentiality must be maintained at all times;")
default_dates = st.session_state.get("def_dates", "April 15, 2025")

# User Input Form
with st.container():
    document_type = st.text_input(
        "Document Type (Ex. Agreement, Contract, NDA)",
        value=default_doc_type,
        help="Specify the title or classification of legal document you require."
    )
    
    parties = st.text_area(
        "Parties Involved",
        value=default_parties,
        height=90,
        help="Names, designations, and roles of the involved parties (e.g. John Doe (Contractor), Acme Corp (Client))."
    )
    
    terms = st.text_area(
        "Terms & Conditions (Use semicolons for bullet points)",
        value=default_terms,
        height=130,
        help="Specific clauses, obligations, payment terms, or covenants separated by semicolons."
    )
    
    dates = st.text_input(
        "Effective Date",
        value=default_dates,
        help="The legal execution or commencement date of this agreement."
    )

# Generation Trigger
generate_clicked = st.button("🚀 Generate Document", type="primary")

if generate_clicked:
    if not document_type.strip() or not parties.strip():
        st.error("Please provide both Document Type and Parties Involved before generating.")
    else:
        with st.spinner("Drafting professional legal document via Gemini AI..."):
            payload = {
                "document_type": document_type.strip(),
                "parties": parties.strip(),
                "terms": terms.strip(),
                "dates": dates.strip()
            }
            generated_doc = ""
            
            # Attempt to call FastAPI backend
            try:
                backend_url = f"{API_BASE_URL.rstrip('/')}/generate"
                res = requests.post(backend_url, json=payload, timeout=25)
                if res.status_code == 200:
                    data = res.json()
                    generated_doc = data.get("document", "")
                else:
                    st.warning(f"Backend returned status {res.status_code}. Processing via direct core generator.")
            except Exception:
                # Fallback to direct core generator
                pass
            
            # If backend not reachable or returned empty, use direct generator
            if not generated_doc:
                fallback_gen = GeminiDocumentGenerator()
                generated_doc = fallback_gen.generate_document(
                    document_type=payload["document_type"],
                    parties=payload["parties"],
                    terms=payload["terms"],
                    dates=payload["dates"]
                )

            sanitized = sanitize_text(generated_doc)
            st.session_state.generated_text = sanitized
            st.success("✅ Document Generated Successfully!")

# Display Output and Actions
if st.session_state.generated_text:
    st.markdown("---")
    
    # Styled HTML Preview
    styled_html = format_html_preview(st.session_state.generated_text)
    st.markdown(styled_html, unsafe_allow_html=True)
    
    st.write("")
    
    # Toggle Inline Editor
    edit_col1, edit_col2 = st.columns([1, 1])
    with edit_col1:
        if st.button("📝 Click to Edit Document"):
            st.session_state.show_edit = not st.session_state.show_edit
            st.rerun()

    if st.session_state.show_edit:
        st.markdown("##### ✏️ Customization & Revision Editor")
        edited_text = st.text_area(
            "Edit Document Below:",
            value=st.session_state.generated_text,
            height=320,
            help="Make any manual adjustments, clause modifications, or custom legal stipulations here."
        )
        if edited_text != st.session_state.generated_text:
            st.session_state.generated_text = sanitize_text(edited_text)
            st.info("Document content updated with your revisions.")

    # Multi-Format Downloads
    st.markdown("### 📥 Download Document")
    file_slug = document_type.strip().lower().replace(" ", "_").replace("/", "_")
    if not file_slug:
        file_slug = "legal_document"

    dcol1, dcol2, dcol3 = st.columns(3)
    
    # 1. Plain Text (.txt)
    with dcol1:
        st.download_button(
            label="📄 Download as .TXT",
            data=st.session_state.generated_text,
            file_name=f"{file_slug}.txt",
            mime="text/plain",
            use_container_width=True
        )

    # 2. Formatted Microsoft Word (.docx)
    with dcol2:
        try:
            docx_data = format_docx(st.session_state.generated_text, doc_type=document_type)
            st.download_button(
                label="📘 Download as .DOCX",
                data=docx_data,
                file_name=f"{file_slug}.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                use_container_width=True
            )
        except Exception as e:
            st.error(f"Error preparing DOCX: {e}")

    # 3. Branded PDF (.pdf)
    with dcol3:
        try:
            pdf_data = format_pdf(st.session_state.generated_text, doc_type=document_type)
            st.download_button(
                label="📕 Download as .PDF",
                data=pdf_data,
                file_name=f"{file_slug}.pdf",
                mime="application/pdf",
                use_container_width=True
            )
        except Exception as e:
            st.error(f"Error preparing PDF: {e}")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #64748b; font-size: 12px;'>"
    "LegalEase Inc. &copy; 2026 | Built for SmartBridge Capstone | Powered by FastAPI & Google Gemini"
    "</div>",
    unsafe_allow_html=True
)
