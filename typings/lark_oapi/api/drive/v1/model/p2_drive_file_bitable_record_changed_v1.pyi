from .bitable_table_record_action import BitableTableRecordAction as BitableTableRecordAction
from .user_id import UserId as UserId
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2DriveFileBitableRecordChangedV1Data:
    file_type: str | None
    file_token: str | None
    table_id: str | None
    revision: int | None
    operator_id: UserId | None
    action_list: list[BitableTableRecordAction] | None
    subscriber_id_list: list[UserId] | None
    update_time: int | None
    def __init__(self, d=None) -> None: ...

class P2DriveFileBitableRecordChangedV1(EventContext):
    event: P2DriveFileBitableRecordChangedV1Data | None
    def __init__(self, d=None) -> None: ...
