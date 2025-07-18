from .update_user_id_user_request_body import UpdateUserIdUserRequestBody as UpdateUserIdUserRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class UpdateUserIdUserRequest(BaseRequest):
    user_id_type: str | None
    user_id: str | None
    request_body: UpdateUserIdUserRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> UpdateUserIdUserRequestBuilder: ...

class UpdateUserIdUserRequestBuilder:
    def __init__(self) -> None: ...
    def user_id_type(self, user_id_type: str) -> UpdateUserIdUserRequestBuilder: ...
    def user_id(self, user_id: str) -> UpdateUserIdUserRequestBuilder: ...
    def request_body(self, request_body: UpdateUserIdUserRequestBody) -> UpdateUserIdUserRequestBuilder: ...
    def build(self) -> UpdateUserIdUserRequest: ...
