from .req_app import ReqApp as ReqApp
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class CreateAppRequest(BaseRequest):
    request_body: ReqApp | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> CreateAppRequestBuilder: ...

class CreateAppRequestBuilder:
    def __init__(self) -> None: ...
    def request_body(self, request_body: ReqApp) -> CreateAppRequestBuilder: ...
    def build(self) -> CreateAppRequest: ...
