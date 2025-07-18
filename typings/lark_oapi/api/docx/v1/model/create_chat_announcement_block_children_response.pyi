from .create_chat_announcement_block_children_response_body import CreateChatAnnouncementBlockChildrenResponseBody as CreateChatAnnouncementBlockChildrenResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateChatAnnouncementBlockChildrenResponse(BaseResponse):
    data: CreateChatAnnouncementBlockChildrenResponseBody | None
    def __init__(self, d=None) -> None: ...
