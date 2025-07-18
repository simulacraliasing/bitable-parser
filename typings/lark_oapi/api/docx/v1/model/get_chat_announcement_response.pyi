from .get_chat_announcement_response_body import GetChatAnnouncementResponseBody as GetChatAnnouncementResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetChatAnnouncementResponse(BaseResponse):
    data: GetChatAnnouncementResponseBody | None
    def __init__(self, d=None) -> None: ...
