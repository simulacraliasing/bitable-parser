from .list_chat_announcement_block_response_body import ListChatAnnouncementBlockResponseBody as ListChatAnnouncementBlockResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListChatAnnouncementBlockResponse(BaseResponse):
    data: ListChatAnnouncementBlockResponseBody | None
    def __init__(self, d=None) -> None: ...
