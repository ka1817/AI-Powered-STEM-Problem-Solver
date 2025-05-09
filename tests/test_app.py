from fastapi.testclient import TestClient
from main import app
import os 
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

client = TestClient(app)

def test_solve_problem_success():
    response = client.post("/solve/", json={"problem": "What is 2 + 3?"})

    assert response.status_code == 200

    data = response.json()
    assert "solution" in data
    assert isinstance(data["solution"], str)

def test_solve_problem_empty_payload():
    response = client.post("/solve/", json={})

    assert response.status_code == 422

