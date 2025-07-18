from .update_block_request import UpdateBlockRequest as UpdateBlockRequest
from lark_oapi.core.construct import init as init

class BatchUpdateChatAnnouncementBlockRequestBody:
    requests: list[UpdateBlockRequest] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> BatchUpdateChatAnnouncementBlockRequestBodyBuilder: ...

class BatchUpdateChatAnnouncementBlockRequestBodyBuilder:
    def __init__(self) -> None: ...
    def requests(self, requests: list[UpdateBlockRequest]) -> BatchUpdateChatAnnouncementBlockRequestBodyBuilder: ...
    def build(self) -> BatchUpdateChatAnnouncementBlockRequestBody: ...
