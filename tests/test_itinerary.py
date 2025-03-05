import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_create_itinerary():
    response = client.post("/itinerary", json={"destination": "Paris", "days": 5})
    assert response.status_code == 200
    assert "itinerary" in response.json()

def test_create_itinerary_invalid_destination():
    response = client.post("/itinerary", json={"destination": "", "days": 5})
    assert response.status_code == 422

def test_create_itinerary_invalid_days():
    response = client.post("/itinerary", json={"destination": "Tokyo", "days": -1})
    assert response.status_code == 422