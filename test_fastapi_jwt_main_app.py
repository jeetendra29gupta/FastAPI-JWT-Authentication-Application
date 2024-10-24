import pytest
from fastapi.testclient import TestClient

from fastapi_jwt_main_app import app


@pytest.fixture
def client():
    """Create a TestClient instance for testing."""
    return TestClient(app)


def test_index(client):
    """Test the welcome endpoint."""
    response = client.get("/")

    # Check if the status code is 200
    assert response.status_code == 200

    # Check if the response contains expected content
    expected_detail = "Welcome to FastAPI JWT Application"
    assert response.json().get("detail") == expected_detail


def test_signup(client):
    """Test the user signup endpoint."""
    user_info = {
        "full_name": "Test User",
        "username": "test_user",
        "password": "test@password"
    }

    response = client.post("/signup", json=user_info)
    # Check if the status code is 201 (Created)
    assert response.status_code == 201
    assert response.json().get("user").get("username") == "test_user"


def test_signup_existing_user(client):
    """Test signup with an already existing username."""
    user_info = {
        "full_name": "Test User",
        "username": "test_user",
        "password": "test@password"
    }

    # First signup to create the user
    client.post("/signup", json=user_info)

    # Attempt to signup with the same username
    response = client.post("/signup", json=user_info)

    # Check if the status code is 400 (Bad Request)
    assert response.status_code == 400
    assert response.json().get("detail") == f"Username: {user_info['username']}, already registered"


def test_login(client):
    """Test the user login endpoint."""
    user_info = {
        "username": "test_user",
        "password": "test@password"
    }

    response = client.post("/login", json=user_info)

    # Check if the status code is 200 (OK)
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert "refresh_token" in response.json()


def test_protected(client):
    """Test the protected endpoint."""
    # Log in to get tokens
    user_info = {
        "username": "test_user",
        "password": "test@password"
    }
    login_response = client.post("/login", json=user_info)
    access_token = login_response.json().get("access_token")

    # Access the protected endpoint with the access token
    response = client.get("/protected", headers={"Authorization": f"Bearer {access_token}"})

    # Check if the status code is 200 (OK)
    assert response.status_code == 200
    assert "message" in response.json()


def test_protected_no_token(client):
    """Test the protected endpoint without a token."""
    response = client.get("/protected")
    # Check if the status code is 401 (Unauthorized)
    assert response.status_code == 422
    expected_detail = [{'input': None, 'loc': ['header', 'authorization'], 'msg': 'Field required', 'type': 'missing'}]
    assert response.json().get("detail") == expected_detail


def test_refresh_token(client):
    """Test the refresh token endpoint."""
    # Log in to get refresh token
    user_info = {
        "username": "test_user",
        "password": "test@password"
    }
    login_response = client.post("/login", json=user_info)
    refresh_token = login_response.json().get("refresh_token")

    # Refresh the access token
    response = client.get("/refresh_token", headers={"Authorization": f"Bearer {refresh_token}"})

    # Check if the status code is 200 (OK)
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_refresh_token_no_token(client):
    """Test the refresh token endpoint without a token."""
    response = client.get("/refresh_token")

    # Check if the status code is 401 (Unauthorized)
    assert response.status_code == 422
    expected_detail = [{'input': None, 'loc': ['header', 'authorization'], 'msg': 'Field required', 'type': 'missing'}]
    assert response.json().get("detail") == expected_detail


if __name__ == "__main__":
    pytest.main()
