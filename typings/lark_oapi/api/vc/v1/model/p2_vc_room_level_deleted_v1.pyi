from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2VcRoomLevelDeletedV1Data:
    room_level_id: str | None
    delete_child: bool | None
    def __init__(self, d=None) -> None: ...

class P2VcRoomLevelDeletedV1(EventContext):
    event: P2VcRoomLevelDeletedV1Data | None
    def __init__(self, d=None) -> None: ...
