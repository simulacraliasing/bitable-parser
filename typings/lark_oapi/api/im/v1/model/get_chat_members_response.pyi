from .get_chat_members_response_body import GetChatMembersResponseBody as GetChatMembersResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetChatMembersResponse(BaseResponse):
    data: GetChatMembersResponseBody | None
    def __init__(self, d=None) -> None: ...
