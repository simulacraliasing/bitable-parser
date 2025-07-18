from .user_id import UserId as UserId
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2AcsAccessRecordCreatedV1Data:
    access_record_id: str | None
    user_id: UserId | None
    device_id: str | None
    is_clock_in: bool | None
    is_door_open: bool | None
    access_time: str | None
    def __init__(self, d=None) -> None: ...

class P2AcsAccessRecordCreatedV1(EventContext):
    event: P2AcsAccessRecordCreatedV1Data | None
    def __init__(self, d=None) -> None: ...
