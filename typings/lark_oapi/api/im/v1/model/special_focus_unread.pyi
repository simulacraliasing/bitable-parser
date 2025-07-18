from lark_oapi.core.construct import init as init

class SpecialFocusUnread:
    id: str | None
    id_type: str | None
    unread_count: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SpecialFocusUnreadBuilder: ...

class SpecialFocusUnreadBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> SpecialFocusUnreadBuilder: ...
    def id_type(self, id_type: str) -> SpecialFocusUnreadBuilder: ...
    def unread_count(self, unread_count: str) -> SpecialFocusUnreadBuilder: ...
    def build(self) -> SpecialFocusUnread: ...
