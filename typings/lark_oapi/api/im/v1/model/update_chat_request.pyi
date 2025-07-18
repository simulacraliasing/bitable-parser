from .update_chat_request_body import UpdateChatRequestBody as UpdateChatRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class UpdateChatRequest(BaseRequest):
    user_id_type: str | None
    chat_id: str | None
    request_body: UpdateChatRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> UpdateChatRequestBuilder: ...

class UpdateChatRequestBuilder:
    def __init__(self) -> None: ...
    def user_id_type(self, user_id_type: str) -> UpdateChatRequestBuilder: ...
    def chat_id(self, chat_id: str) -> UpdateChatRequestBuilder: ...
    def request_body(self, request_body: UpdateChatRequestBody) -> UpdateChatRequestBuilder: ...
    def build(self) -> UpdateChatRequest: ...
