from .copy_app_request_body import CopyAppRequestBody as CopyAppRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class CopyAppRequest(BaseRequest):
    app_token: str | None
    request_body: CopyAppRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> CopyAppRequestBuilder: ...

class CopyAppRequestBuilder:
    def __init__(self) -> None: ...
    def app_token(self, app_token: str) -> CopyAppRequestBuilder: ...
    def request_body(self, request_body: CopyAppRequestBody) -> CopyAppRequestBuilder: ...
    def build(self) -> CopyAppRequest: ...
