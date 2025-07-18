from .room_event import RoomEvent as RoomEvent
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2VcRoomDeletedV1Data:
    room: RoomEvent | None
    def __init__(self, d=None) -> None: ...

class P2VcRoomDeletedV1(EventContext):
    event: P2VcRoomDeletedV1Data | None
    def __init__(self, d=None) -> None: ...
