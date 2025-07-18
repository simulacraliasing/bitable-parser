from lark_oapi.core.construct import init as init

class Due:
    time: int | None
    timezone: str | None
    is_all_day: bool | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DueBuilder: ...

class DueBuilder:
    def __init__(self) -> None: ...
    def time(self, time: int) -> DueBuilder: ...
    def timezone(self, timezone: str) -> DueBuilder: ...
    def is_all_day(self, is_all_day: bool) -> DueBuilder: ...
    def build(self) -> Due: ...
