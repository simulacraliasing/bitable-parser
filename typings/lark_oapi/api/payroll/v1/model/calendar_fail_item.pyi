from lark_oapi.core.construct import init as init

class CalendarFailItem:
    id: str | None
    fail_reason: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CalendarFailItemBuilder: ...

class CalendarFailItemBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> CalendarFailItemBuilder: ...
    def fail_reason(self, fail_reason: str) -> CalendarFailItemBuilder: ...
    def build(self) -> CalendarFailItem: ...
