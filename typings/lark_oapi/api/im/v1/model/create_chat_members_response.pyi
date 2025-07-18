from .create_chat_members_response_body import CreateChatMembersResponseBody as CreateChatMembersResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateChatMembersResponse(BaseResponse):
    data: CreateChatMembersResponseBody | None
    def __init__(self, d=None) -> None: ...
