from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class ReadUserBatchMessageRequest(BaseRequest):
    batch_message_id: str | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> ReadUserBatchMessageRequestBuilder: ...

class ReadUserBatchMessageRequestBuilder:
    def __init__(self) -> None: ...
    def batch_message_id(self, batch_message_id: str) -> ReadUserBatchMessageRequestBuilder: ...
    def build(self) -> ReadUserBatchMessageRequest: ...
