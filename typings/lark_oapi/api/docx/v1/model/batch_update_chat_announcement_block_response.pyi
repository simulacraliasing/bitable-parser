from .batch_update_chat_announcement_block_response_body import BatchUpdateChatAnnouncementBlockResponseBody as BatchUpdateChatAnnouncementBlockResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchUpdateChatAnnouncementBlockResponse(BaseResponse):
    data: BatchUpdateChatAnnouncementBlockResponseBody | None
    def __init__(self, d=None) -> None: ...
