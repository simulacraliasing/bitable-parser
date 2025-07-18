from .block import Block as Block
from lark_oapi.core.construct import init as init

class GetChatAnnouncementBlockChildrenResponseBody:
    items: list[Block] | None
    page_token: str | None
    has_more: bool | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> GetChatAnnouncementBlockChildrenResponseBodyBuilder: ...

class GetChatAnnouncementBlockChildrenResponseBodyBuilder:
    def __init__(self) -> None: ...
    def items(self, items: list[Block]) -> GetChatAnnouncementBlockChildrenResponseBodyBuilder: ...
    def page_token(self, page_token: str) -> GetChatAnnouncementBlockChildrenResponseBodyBuilder: ...
    def has_more(self, has_more: bool) -> GetChatAnnouncementBlockChildrenResponseBodyBuilder: ...
    def build(self) -> GetChatAnnouncementBlockChildrenResponseBody: ...
