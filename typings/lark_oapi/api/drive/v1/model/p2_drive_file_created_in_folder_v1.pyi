from .user_id import UserId as UserId
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2DriveFileCreatedInFolderV1Data:
    file_type: str | None
    file_token: str | None
    folder_token: str | None
    operator_id: UserId | None
    subscriber_ids: list[UserId] | None
    def __init__(self, d=None) -> None: ...

class P2DriveFileCreatedInFolderV1(EventContext):
    event: P2DriveFileCreatedInFolderV1Data | None
    def __init__(self, d=None) -> None: ...
