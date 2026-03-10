import httpx

from httpx_client.constants import HOST, PASSWORD


def login(email: str, password: str) -> dict:
    payload = {"email": email, "password": password}
    response = httpx.post(f"{HOST}/api/v1/authentication/login", json=payload)
    print(response.json())
    print(response.status_code)
    return response.json()


def me(access_token: str):
    headers = {"Authorization": f"Bearer {access_token}"}

    response = httpx.get(f"{HOST}/api/v1/users/me", headers=headers)
    print(response.json())
    print(response.status_code)
    return response.json()


if __name__ == "__main__":
    auth_data = login("gloctarr@example.com", PASSWORD)
    me(auth_data["token"]["accessToken"])
