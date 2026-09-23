import pytest
from ai_core.gemini_generator import GeminiDocumentGenerator
from ai_core.generator import format_docx, format_pdf, format_html_preview

def test_gemini_document_generation():
    generator = GeminiDocumentGenerator()
    doc_type = "Freelance Work Contract"
    parties = "Jane Doe (Provider), TechNova (Client)"
    terms = "Payment within 30 days; Confidentiality strictly observed;"
    date = "April 15, 2025"

    result = generator.generate_document(doc_type, parties, terms, date)
    assert result is not None
    assert len(result) > 100
    assert "FREELANCE WORK CONTRACT" in result or "Freelance Work Contract" in result
    assert "Jane Doe" in result
    assert "TechNova" in result
    assert "April 15, 2025" in result

def test_docx_generation():
    text = "## AGREEMENT\nBetween Party A and Party B\n- Clause 1: Payment on time;\n- Clause 2: Confidentiality;"
    docx_bytes = format_docx(text, doc_type="Agreement")
    assert isinstance(docx_bytes, bytes)
    assert len(docx_bytes) > 500
    # DOCX files are zip archives starting with 'PK\x03\x04'
    assert docx_bytes[:4] == b'PK\x03\x04'

def test_pdf_generation():
    text = "## NON-DISCLOSURE AGREEMENT\nBetween Party A and Party B\n- Confidentiality for 3 years\nSigned by both parties."
    pdf_bytes = format_pdf(text, doc_type="Non-Disclosure Agreement")
    assert isinstance(pdf_bytes, bytes)
    assert len(pdf_bytes) > 500
    # PDF files start with '%PDF'
    assert pdf_bytes[:4] == b'%PDF'

def test_html_preview_generation():
    text = "## Section 1\nThis is a sample clause.\n- Item 1\n- Item 2"
    html = format_html_preview(text)
    assert "<h3" in html
    assert "OFFICIAL LEGAL PREVIEW" in html
    assert "Item 1" in html
