from .get_chat_announcement_block_response_body import GetChatAnnouncementBlockResponseBody as GetChatAnnouncementBlockResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetChatAnnouncementBlockResponse(BaseResponse):
    data: GetChatAnnouncementBlockResponseBody | None
    def __init__(self, d=None) -> None: ...
