from .create_identity_request_body import CreateIdentityRequestBody as CreateIdentityRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class CreateIdentityRequest(BaseRequest):
    user_id: str | None
    user_id_type: str | None
    request_body: CreateIdentityRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> CreateIdentityRequestBuilder: ...

class CreateIdentityRequestBuilder:
    def __init__(self) -> None: ...
    def user_id(self, user_id: str) -> CreateIdentityRequestBuilder: ...
    def user_id_type(self, user_id_type: str) -> CreateIdentityRequestBuilder: ...
    def request_body(self, request_body: CreateIdentityRequestBody) -> CreateIdentityRequestBuilder: ...
    def build(self) -> CreateIdentityRequest: ...
