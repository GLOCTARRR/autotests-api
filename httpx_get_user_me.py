import httpx


def login(email: str, password: str) -> dict:
    payload = {"email": email, "password": password}
    response = httpx.post(
        "http://localhost:8000/api/v1/authentication/login", json=payload
    )
    print(response.json())
    print(response.status_code)
    return response.json()


def me(access_token: str):
    headers = {"Authorization": f"Bearer {access_token}"}
    response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
    print(response.json())
    print(response.status_code)
    return response.json()


if __name__ == "__main__":
    auth_data = login("gloctarr@example.com", "123456")
    me(auth_data["token"]["accessToken"])
