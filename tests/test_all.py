from api_client import get users, create_user, login_user


def test_get_user():
    response = get_users()

    assert response.status_code == 200

    print(data)

    data = response.json()
    assert "data" in data
    assert len(data["data"]) > 0