from .delete_tabs_chat_tab_request_body import DeleteTabsChatTabRequestBody as DeleteTabsChatTabRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class DeleteTabsChatTabRequest(BaseRequest):
    chat_id: str | None
    request_body: DeleteTabsChatTabRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> DeleteTabsChatTabRequestBuilder: ...

class DeleteTabsChatTabRequestBuilder:
    def __init__(self) -> None: ...
    def chat_id(self, chat_id: str) -> DeleteTabsChatTabRequestBuilder: ...
    def request_body(self, request_body: DeleteTabsChatTabRequestBody) -> DeleteTabsChatTabRequestBuilder: ...
    def build(self) -> DeleteTabsChatTabRequest: ...
