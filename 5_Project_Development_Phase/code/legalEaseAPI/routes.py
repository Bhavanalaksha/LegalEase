from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from ai_core.gemini_generator import GeminiDocumentGenerator

router = APIRouter(prefix="", tags=["Legal Documents"])

# Initialize Gemini AI Document Generator
gemini_generator = GeminiDocumentGenerator()

class DocumentRequest(BaseModel):
    document_type: str = Field(..., description="Type of legal document e.g. Contract, NDA, Lease Agreement", json_schema_extra={"example": "Freelance Work Contract"})
    parties: str = Field(..., description="Names and roles of the involved parties", json_schema_extra={"example": "Jane Doe (Service Provider), TechNova Inc. (Client)"})
    terms: str = Field(..., description="Terms and conditions separated by semicolons or bullet points", json_schema_extra={"example": "Payment to be made within 30 days of invoice; The provider agrees to deliver work by agreed deadline; Confidentiality must be maintained at all times;"})
    dates: str = Field(..., description="Effective date for the legal agreement", json_schema_extra={"example": "April 15, 2025"})

class DocumentResponse(BaseModel):
    document: str
    status: str = "success"

@router.post("/generate", response_model=DocumentResponse)
def generate_legal_document(request: DocumentRequest):
    """
    Endpoint to generate a structured, formal legal document based on user inputs.
    """
    try:
        response = gemini_generator.generate_document(
            document_type=request.document_type,
            parties=request.parties,
            terms=request.terms,
            dates=request.dates
        )
        return DocumentResponse(document=response, status="success")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Generation failed: {str(e)}")
