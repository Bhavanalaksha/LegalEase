import pytest
from fastapi.testclient import TestClient
from legalEaseAPI.main import app

client = TestClient(app)

def test_api_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert data["status"] == "online"
    assert "LegalEase" in data["message"]

def test_api_generate_endpoint_success():
    payload = {
        "document_type": "Freelance Work Contract",
        "parties": "Jane Doe (Provider), TechNova Inc. (Client)",
        "terms": "Payment within 15 days; IP transferred to client;",
        "dates": "April 15, 2025"
    }
    response = client.post("/generate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "document" in data
    assert len(data["document"]) > 50

def test_api_generate_missing_field():
    # Missing 'parties'
    payload = {
        "document_type": "Freelance Work Contract",
        "terms": "Payment within 15 days;",
        "dates": "April 15, 2025"
    }
    response = client.post("/generate", json=payload)
    assert response.status_code == 422 # Unprocessable Entity
