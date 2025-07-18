from lark_oapi.core.construct import init as init

class CalendarFreebusy:
    start_time: str | None
    end_time: str | None
    calendar_id: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CalendarFreebusyBuilder: ...

class CalendarFreebusyBuilder:
    def __init__(self) -> None: ...
    def start_time(self, start_time: str) -> CalendarFreebusyBuilder: ...
    def end_time(self, end_time: str) -> CalendarFreebusyBuilder: ...
    def calendar_id(self, calendar_id: str) -> CalendarFreebusyBuilder: ...
    def build(self) -> CalendarFreebusy: ...
