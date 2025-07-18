from .create_chat_members_request_body import CreateChatMembersRequestBody as CreateChatMembersRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class CreateChatMembersRequest(BaseRequest):
    member_id_type: str | None
    succeed_type: int | None
    chat_id: str | None
    request_body: CreateChatMembersRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> CreateChatMembersRequestBuilder: ...

class CreateChatMembersRequestBuilder:
    def __init__(self) -> None: ...
    def member_id_type(self, member_id_type: str) -> CreateChatMembersRequestBuilder: ...
    def succeed_type(self, succeed_type: int) -> CreateChatMembersRequestBuilder: ...
    def chat_id(self, chat_id: str) -> CreateChatMembersRequestBuilder: ...
    def request_body(self, request_body: CreateChatMembersRequestBody) -> CreateChatMembersRequestBuilder: ...
    def build(self) -> CreateChatMembersRequest: ...
