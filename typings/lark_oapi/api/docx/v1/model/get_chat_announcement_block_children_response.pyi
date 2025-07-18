from .get_chat_announcement_block_children_response_body import GetChatAnnouncementBlockChildrenResponseBody as GetChatAnnouncementBlockChildrenResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetChatAnnouncementBlockChildrenResponse(BaseResponse):
    data: GetChatAnnouncementBlockChildrenResponseBody | None
    def __init__(self, d=None) -> None: ...
