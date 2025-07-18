from .create_app_request_body import CreateAppRequestBody as CreateAppRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class CreateAppRequest(BaseRequest):
    user_id_type: str | None
    page_size: int | None
    page_token: str | None
    request_body: CreateAppRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> CreateAppRequestBuilder: ...

class CreateAppRequestBuilder:
    def __init__(self) -> None: ...
    def user_id_type(self, user_id_type: str) -> CreateAppRequestBuilder: ...
    def page_size(self, page_size: int) -> CreateAppRequestBuilder: ...
    def page_token(self, page_token: str) -> CreateAppRequestBuilder: ...
    def request_body(self, request_body: CreateAppRequestBody) -> CreateAppRequestBuilder: ...
    def build(self) -> CreateAppRequest: ...
