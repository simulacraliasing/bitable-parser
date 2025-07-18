from .create_chat_request_body import CreateChatRequestBody as CreateChatRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class CreateChatRequest(BaseRequest):
    user_id_type: str | None
    set_bot_manager: bool | None
    uuid: str | None
    request_body: CreateChatRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> CreateChatRequestBuilder: ...

class CreateChatRequestBuilder:
    def __init__(self) -> None: ...
    def user_id_type(self, user_id_type: str) -> CreateChatRequestBuilder: ...
    def set_bot_manager(self, set_bot_manager: bool) -> CreateChatRequestBuilder: ...
    def uuid(self, uuid: str) -> CreateChatRequestBuilder: ...
    def request_body(self, request_body: CreateChatRequestBody) -> CreateChatRequestBuilder: ...
    def build(self) -> CreateChatRequest: ...
