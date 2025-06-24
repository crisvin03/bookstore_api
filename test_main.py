from fastapi.testclient import TestClient
from main import app

# Creating a test client using FastAPI's built-in TestClient
client = TestClient(app)

#Test the root endpoint ("/") for correct welcome message
def test_read_root():
    response = client.get("/")  
    assert response.status_code == 200  
    data = response.json()  
    assert "message" in data  
    assert "Bookstore API" in data["message"]
