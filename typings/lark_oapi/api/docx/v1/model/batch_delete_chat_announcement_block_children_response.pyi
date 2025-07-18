from .batch_delete_chat_announcement_block_children_response_body import BatchDeleteChatAnnouncementBlockChildrenResponseBody as BatchDeleteChatAnnouncementBlockChildrenResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchDeleteChatAnnouncementBlockChildrenResponse(BaseResponse):
    data: BatchDeleteChatAnnouncementBlockChildrenResponseBody | None
    def __init__(self, d=None) -> None: ...
