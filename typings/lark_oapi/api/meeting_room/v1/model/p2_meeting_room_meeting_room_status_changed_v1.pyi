from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2MeetingRoomMeetingRoomStatusChangedV1Data:
    room_name: str | None
    room_id: str | None
    def __init__(self, d=None) -> None: ...

class P2MeetingRoomMeetingRoomStatusChangedV1(EventContext):
    event: P2MeetingRoomMeetingRoomStatusChangedV1Data | None
    def __init__(self, d=None) -> None: ...
