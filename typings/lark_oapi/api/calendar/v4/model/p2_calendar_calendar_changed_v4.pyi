from .user_id import UserId as UserId
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CalendarCalendarChangedV4Data:
    user_id_list: list[UserId] | None
    def __init__(self, d=None) -> None: ...

class P2CalendarCalendarChangedV4(EventContext):
    event: P2CalendarCalendarChangedV4Data | None
    def __init__(self, d=None) -> None: ...
