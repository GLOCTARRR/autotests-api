import httpx

from httpx_client.constants import HOST


def login(email, password):
    payload = {
        "email": email,
        "password": password
    }
    response = httpx.post(f"{HOST}/api/v1/authentication/login", json=payload)
    print(response.json())
    print(response.status_code)
    return response.json()

def me(access_token):
    headers = {"Authorization": f"Bearer {access_token}"}

    response = httpx.get(f"{HOST}/api/v1/users/me", headers=headers)
    print(response.json())
    print(response.status_code)
    return response.json()

if __name__ == "__main__":
    auth_data = login("gloctarr@example.com", "123456")
    me(auth_data["token"]["accessToken"])

