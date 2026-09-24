import io
import re
import os
from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from fpdf import FPDF
from config import LOGO_PATH, BASE_DIR

def sanitize_text(text: str) -> str:
    """
    Sanitize text by normalizing smart quotes, em-dashes, and special characters
    to ensure seamless export across PDF, DOCX, and TXT.
    """
    if not text:
        return ""
    
    # Replace curly quotes and apostrophes
    replacements = {
        '“': '"',
        '”': '"',
        '‘': "'",
        '’': "'",
        '—': ' - ',
        '–': ' - ',
        '…': '...',
        '\u00a0': ' ', # non-breaking space
        '\t': '    ',
        '\r\n': '\n'
    }
    sanitized = text
    for orig, rep in replacements.items():
        sanitized = sanitized.replace(orig, rep)
    
    return sanitized.strip()


def format_docx(text: str, doc_type: str = "Legal Document") -> bytes:
    """
    Generates a professionally styled Microsoft Word (.docx) document:
    - Times New Roman font
    - Center-embedded LegalEase Logo on the front page
    - Formatted document title and headings
    - Structured terms table
    - Execution & signature block
    - Formal footer
    """
    doc = Document()
    
    # Set page margins to standard legal 1-inch
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        
        # Add footer
        footer = section.footer
        footer_para = footer.paragraphs[0]
        footer_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        footer_run = footer_para.add_run("LegalEase Inc. | contact@legalease.com | All Rights Reserved.")
        footer_run.font.name = "Times New Roman"
        footer_run.font.size = Pt(9)
        footer_run.font.color.rgb = RGBColor(128, 128, 128)

    # 1. Embed Logo at the top if exists
    if LOGO_PATH and LOGO_PATH.exists():
        logo_para = doc.add_paragraph()
        logo_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        logo_run = logo_para.add_run()
        try:
            logo_run.add_picture(str(LOGO_PATH), width=Inches(2.5))
        except Exception as e:
            print(f"[Warning] Could not insert docx logo: {e}")

    # 2. Main Title
    title_para = doc.add_paragraph()
    title_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title_run = title_para.add_run(doc_type.upper())
    title_run.font.name = "Times New Roman"
    title_run.font.size = Pt(18)
    title_run.font.bold = True
    title_run.font.color.rgb = RGBColor(26, 37, 48)
    title_para.paragraph_format.space_after = Pt(18)

    # 3. Process Content Lines
    lines = sanitize_text(text).split('\n')
    terms_buffer = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        
        # Heading 1 / 2
        if stripped.startswith("## ") or stripped.startswith("### "):
            clean_heading = stripped.lstrip("#").strip()
            # If skipping redundant main title
            if clean_heading.upper() == doc_type.upper():
                continue
            h_para = doc.add_paragraph()
            h_run = h_para.add_run(clean_heading)
            h_run.font.name = "Times New Roman"
            h_run.font.size = Pt(13)
            h_run.font.bold = True
            h_run.font.color.rgb = RGBColor(30, 41, 59)
            h_para.paragraph_format.space_before = Pt(12)
            h_para.paragraph_format.space_after = Pt(4)
        
        # Bullet list / clauses
        elif stripped.startswith("- ") or stripped.startswith("* ") or (len(stripped) > 2 and stripped[:2].isdigit() and stripped[2] == '.'):
            bullet_text = re.sub(r'^[-*]\s+|\*\*', '', stripped).replace('**', '')
            p = doc.add_paragraph(style='List Bullet')
            r = p.add_run(bullet_text)
            r.font.name = "Times New Roman"
            r.font.size = Pt(11)
            p.paragraph_format.space_after = Pt(3)
            
            # Check if line looks like a specific term clause for table summary
            if "clause" in bullet_text.lower() or "payment" in bullet_text.lower() or "deadline" in bullet_text.lower() or "confidential" in bullet_text.lower():
                terms_buffer.append(bullet_text)

        elif stripped == "---":
            continue

        else:
            # Regular paragraph
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            # Parse bold spans
            parts = re.split(r'(\*\*.*?\*\*)', stripped)
            for part in parts:
                if part.startswith("**") and part.endswith("**"):
                    r = p.add_run(part[2:-2])
                    r.font.bold = True
                else:
                    r = p.add_run(part)
                r.font.name = "Times New Roman"
                r.font.size = Pt(11)
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_after = Pt(6)

    # 4. If we extracted key terms, insert a Summary Table of Terms as requested in spec
    if terms_buffer and len(terms_buffer) >= 2:
        table_title = doc.add_paragraph()
        tt_run = table_title.add_run("Summary Table of Agreed Terms")
        tt_run.font.name = "Times New Roman"
        tt_run.font.size = Pt(12)
        tt_run.font.bold = True
        table_title.paragraph_format.space_before = Pt(12)
        table_title.paragraph_format.space_after = Pt(4)

        table = doc.add_table(rows=1, cols=2)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = "Item #"
        hdr_cells[1].text = "Agreed Covenant / Term"
        for i, cell in enumerate(hdr_cells):
            cell.paragraphs[0].runs[0].font.name = "Times New Roman"
            cell.paragraphs[0].runs[0].font.bold = True
            cell.paragraphs[0].runs[0].font.size = Pt(10)

        for i, term in enumerate(terms_buffer[:6]):
            row_cells = table.add_row().cells
            row_cells[0].text = f"T-{i+1:02d}"
            row_cells[1].text = term
            for cell in row_cells:
                for p in cell.paragraphs:
                    for r in p.runs:
                        r.font.name = "Times New Roman"
                        r.font.size = Pt(9.5)

    buffer = io.BytesIO()
    doc.save(buffer)
    return buffer.getvalue()


class LegalPDF(FPDF):
    """
    Custom FPDF class with branded header and footer matching LegalEase specifications.
    """
    def __init__(self, doc_type: str = "Legal Document", logo_path: str = None):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.doc_type = doc_type
        self.logo_path = logo_path
        self.set_auto_page_break(auto=True, margin=20)

    def header(self):
        if self.logo_path and os.path.exists(self.logo_path):
            try:
                # Center logo at top
                self.image(self.logo_path, x=(self.w - 50) / 2, y=8, w=50)
                self.ln(18)
            except Exception:
                pass
        self.set_font("Times", "B", 14)
        self.set_text_color(26, 37, 48)
        self.cell(0, 8, self.doc_type.upper(), border=0, align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(200, 200, 200)
        self.line(20, self.get_y(), self.w - 20, self.get_y())
        self.ln(6)

    def footer(self):
        self.set_y(-15)
        self.set_font("Times", "I", 8)
        self.set_text_color(128, 128, 128)
        footer_text = f"LegalEase Inc. | contact@legalease.com | All Rights Reserved.    Page {self.page_no()}"
        self.cell(0, 8, footer_text, align="C")


def format_pdf(text: str, doc_type: str = "Legal Document") -> bytes:
    """
    Generates a branded PDF using fpdf2 with header, footer, logo, and clean typography.
    """
    logo_file = str(LOGO_PATH) if LOGO_PATH and LOGO_PATH.exists() else None
    pdf = LegalPDF(doc_type=doc_type, logo_path=logo_file)
    pdf.add_page()
    pdf.set_margins(left=20, top=20, right=20)
    pdf.set_font("Times", size=10)

    lines = sanitize_text(text).split('\n')

    for line in lines:
        stripped = line.strip()
        if not stripped:
            pdf.ln(3)
            continue

        # Skip duplicate main title in body
        if stripped.startswith("## ") and stripped.lstrip("#").strip().upper() == doc_type.upper():
            continue

        # Heading 2 / 3
        if stripped.startswith("## ") or stripped.startswith("### "):
            pdf.ln(3)
            heading_text = stripped.lstrip("#").strip()
            pdf.set_font("Times", "B", 11)
            pdf.set_text_color(30, 41, 59)
            pdf.multi_cell(0, 6, heading_text)
            pdf.set_font("Times", size=10)
            pdf.set_text_color(20, 20, 20)
            pdf.ln(1)

        # Bullet items
        elif stripped.startswith("- ") or stripped.startswith("* "):
            clean_item = stripped[2:].strip().replace('**', '')
            pdf.set_font("Times", size=10)
            pdf.set_text_color(40, 40, 40)
            # Indented bullet
            pdf.cell(5, 5, chr(149), align="R") # bullet symbol or dash
            pdf.multi_cell(0, 5, f"  {clean_item}")
            pdf.ln(1)

        elif stripped == "---":
            pdf.ln(2)
            y = pdf.get_y()
            pdf.set_draw_color(220, 220, 220)
            pdf.line(20, y, pdf.w - 20, y)
            pdf.ln(3)

        else:
            # Paragraph
            pdf.set_font("Times", size=10)
            pdf.set_text_color(30, 30, 30)
            clean_para = stripped.replace('**', '')
            pdf.multi_cell(0, 5.2, clean_para, align="J")
            pdf.ln(2)

    return bytes(pdf.output())


def format_html_preview(text: str) -> str:
    """
    Converts raw generated document text into an elegant, styled HTML preview container
    matching the dark-theme UI specifications of LegalEase.
    """
    if not text:
        return "<em>No document content generated yet.</em>"

    sanitized = sanitize_text(text)
    
    # Process markdown headings to styled divs
    html_lines = []
    for line in sanitized.split('\n'):
        line_s = line.strip()
        if not line_s:
            html_lines.append("<div style='height: 8px;'></div>")
        elif line_s.startswith("## "):
            title = line_s.lstrip("#").strip()
            html_lines.append(f"<h3 style='color: #38bdf8; border-bottom: 1px solid #334155; padding-bottom: 4px; margin-top: 16px; margin-bottom: 8px; font-family: Georgia, serif;'>{title}</h3>")
        elif line_s.startswith("### "):
            sub = line_s.lstrip("#").strip()
            html_lines.append(f"<h4 style='color: #f1f5f9; margin-top: 14px; margin-bottom: 6px; font-weight: 600; font-family: Georgia, serif;'>{sub}</h4>")
        elif line_s.startswith("- ") or line_s.startswith("* "):
            item = line_s[2:].strip()
            # replace markdown bold
            item = re.sub(r'\*\*(.*?)\*\*', r'<strong style="color: #e2e8f0;">\1</strong>', item)
            html_lines.append(f"<li style='color: #cbd5e1; margin-left: 20px; line-height: 1.6;'>{item}</li>")
        elif line_s == "---":
            html_lines.append("<hr style='border: 0; border-top: 1px solid #475569; margin: 16px 0;'/>")
        else:
            para = re.sub(r'\*\*(.*?)\*\*', r'<strong style="color: #f8fafc;">\1</strong>', line_s)
            html_lines.append(f"<p style='color: #94a3b8; line-height: 1.7; margin-bottom: 8px; font-size: 14px;'>{para}</p>")

    styled_html = f"""
    <div style="background-color: #0f172a; color: #f8fafc; padding: 24px; border-radius: 10px; border: 1px solid #1e293b; box-shadow: 0 4px 12px rgba(0,0,0,0.4); max-height: 520px; overflow-y: auto; font-family: 'Times New Roman', Times, serif;">
        <div style="text-align: center; margin-bottom: 16px;">
            <span style="font-size: 11px; letter-spacing: 2px; text-transform: uppercase; color: #94a3b8; background: #1e293b; padding: 3px 10px; border-radius: 4px;">OFFICIAL LEGAL PREVIEW</span>
        </div>
        {''.join(html_lines)}
    </div>
    """
    return styled_html
