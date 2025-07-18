from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class SubscribeFileRequest(BaseRequest):
    file_type: str | None
    event_type: str | None
    file_token: str | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> SubscribeFileRequestBuilder: ...

class SubscribeFileRequestBuilder:
    def __init__(self) -> None: ...
    def file_type(self, file_type: str) -> SubscribeFileRequestBuilder: ...
    def event_type(self, event_type: str) -> SubscribeFileRequestBuilder: ...
    def file_token(self, file_token: str) -> SubscribeFileRequestBuilder: ...
    def build(self) -> SubscribeFileRequest: ...
