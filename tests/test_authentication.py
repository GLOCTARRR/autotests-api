from http import HTTPStatus
import pytest

from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import (
    LoginRequestSchema,
    LoginResponseSchema,
)
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.authentication
def test_login():
    public_users_client = get_public_users_client()

    create_user_request = CreateUserRequestSchema()
    public_users_client.create_user(create_user_request)

    authentication_client = get_authentication_client()

    request = LoginRequestSchema(
        email=create_user_request.email, password=create_user_request.password
    )
    response = authentication_client.login_api(request)
    response_data = LoginResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_login_response(response_data)

    validate_json_schema(response.json(), response_data.model_json_schema())
