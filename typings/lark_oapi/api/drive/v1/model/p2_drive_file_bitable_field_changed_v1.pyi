from .bitable_table_field_action import BitableTableFieldAction as BitableTableFieldAction
from .user_id import UserId as UserId
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2DriveFileBitableFieldChangedV1Data:
    file_type: str | None
    file_token: str | None
    table_id: str | None
    operator_id: UserId | None
    action_list: list[BitableTableFieldAction] | None
    revision: int | None
    subscriber_id_list: list[UserId] | None
    update_time: int | None
    def __init__(self, d=None) -> None: ...

class P2DriveFileBitableFieldChangedV1(EventContext):
    event: P2DriveFileBitableFieldChangedV1Data | None
    def __init__(self, d=None) -> None: ...
