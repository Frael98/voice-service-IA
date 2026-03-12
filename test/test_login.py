def test_login_success(client):

    response = client.post(
        "/v1/auth/login",
        json={
            "username": "admin",
            "password": "123456"
        }
    )

    assert response.status_code == 200
    assert "access_token" in response.json()


def test_login_invalid(client):

    response = client.post(
        "/v1/auth/login",
        json={
            "username": "admin",
            "password": "asffg"
        }
    )

    assert response.status_code == 401