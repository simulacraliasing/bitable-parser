from lark_oapi.core.construct import init as init

class CalendarByScopeLeaveResponseBody:
    calendar_wk_id: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CalendarByScopeLeaveResponseBodyBuilder: ...

class CalendarByScopeLeaveResponseBodyBuilder:
    def __init__(self) -> None: ...
    def calendar_wk_id(self, calendar_wk_id: str) -> CalendarByScopeLeaveResponseBodyBuilder: ...
    def build(self) -> CalendarByScopeLeaveResponseBody: ...
