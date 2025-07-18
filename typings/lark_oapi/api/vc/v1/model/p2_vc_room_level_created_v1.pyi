from .room_level import RoomLevel as RoomLevel
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2VcRoomLevelCreatedV1Data:
    room_level: RoomLevel | None
    def __init__(self, d=None) -> None: ...

class P2VcRoomLevelCreatedV1(EventContext):
    event: P2VcRoomLevelCreatedV1Data | None
    def __init__(self, d=None) -> None: ...
