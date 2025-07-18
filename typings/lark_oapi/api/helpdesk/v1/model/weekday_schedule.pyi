from lark_oapi.core.construct import init as init

class WeekdaySchedule:
    start_time: str | None
    end_time: str | None
    weekday: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> WeekdayScheduleBuilder: ...

class WeekdayScheduleBuilder:
    def __init__(self) -> None: ...
    def start_time(self, start_time: str) -> WeekdayScheduleBuilder: ...
    def end_time(self, end_time: str) -> WeekdayScheduleBuilder: ...
    def weekday(self, weekday: int) -> WeekdayScheduleBuilder: ...
    def build(self) -> WeekdaySchedule: ...
