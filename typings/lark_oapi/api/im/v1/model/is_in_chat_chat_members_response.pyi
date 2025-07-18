from .is_in_chat_chat_members_response_body import IsInChatChatMembersResponseBody as IsInChatChatMembersResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class IsInChatChatMembersResponse(BaseResponse):
    data: IsInChatChatMembersResponseBody | None
    def __init__(self, d=None) -> None: ...
