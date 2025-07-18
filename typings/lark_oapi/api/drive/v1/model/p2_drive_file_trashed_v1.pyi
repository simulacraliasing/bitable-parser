from .user_id import UserId as UserId
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2DriveFileTrashedV1Data:
    file_type: str | None
    file_token: str | None
    operator_id: UserId | None
    subscriber_id_list: list[UserId] | None
    def __init__(self, d=None) -> None: ...

class P2DriveFileTrashedV1(EventContext):
    event: P2DriveFileTrashedV1Data | None
    def __init__(self, d=None) -> None: ...
