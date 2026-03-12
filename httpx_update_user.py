import httpx

from utils import data_utils


def login(email: str, password: str) -> dict:
    print("___login___:")
    payload = {"email": email, "password": password}
    response = httpx.post(
        "http://localhost:8000/api/v1/authentication/login", json=payload
    )
    print(response.json())
    print(response.status_code)
    return response.json()


def create_user(user_data: dict) -> dict:
    print("___create_user___:")
    response = httpx.post("http://localhost:8000/api/v1/users", json=user_data)
    print(response.json())
    print(response.status_code)
    return response.json()


def update_user(user_id: str, user_data: dict, access_token: str) -> dict:
    print("___update_user___:")
    headers = {"Authorization": f"Bearer {access_token}"}

    response = httpx.patch(
        f"http://localhost:8000/api/v1/users/{user_id}", json=user_data, headers=headers
    )
    print(response.json())
    print(response.status_code)
    return response.json()


if __name__ == "__main__":
    password = "123456"
    user_data = {
        "email": data_utils.generate_email(),
        "password": password,
        "lastName": data_utils.generate_string(),
        "firstName": data_utils.generate_string(),
        "middleName": data_utils.generate_string(),
    }

    created_user_data = create_user(user_data)
    auth_data = login(user_data["email"], password)

    new_user_data = {
        "email": data_utils.generate_email(),
        "lastName": data_utils.generate_string(),
        "firstName": data_utils.generate_string(),
        "middleName": data_utils.generate_string(),
    }

    update_user(
        user_id=created_user_data["user"]["id"],
        user_data=new_user_data,
        access_token=auth_data["token"]["accessToken"],
    )
