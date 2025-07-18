from .open_event_rsvp_info import OpenEventRsvpInfo as OpenEventRsvpInfo
from .user_id import UserId as UserId
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CalendarCalendarEventChangedV4Data:
    calendar_id: str | None
    user_id_list: list[UserId] | None
    calendar_event_id: str | None
    change_type: str | None
    rsvp_infos: list[OpenEventRsvpInfo] | None
    def __init__(self, d=None) -> None: ...

class P2CalendarCalendarEventChangedV4(EventContext):
    event: P2CalendarCalendarEventChangedV4Data | None
    def __init__(self, d=None) -> None: ...
