from .user_id import UserId as UserId
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2DriveFilePermissionMemberAppliedV1Data:
    file_type: str | None
    file_token: str | None
    operator_id: UserId | None
    approver_id: UserId | None
    application_user_list: list[UserId] | None
    application_chat_list: list[str] | None
    application_department_list: list[str] | None
    application_remark: str | None
    permission: str | None
    subscriber_ids: list[UserId] | None
    def __init__(self, d=None) -> None: ...

class P2DriveFilePermissionMemberAppliedV1(EventContext):
    event: P2DriveFilePermissionMemberAppliedV1Data | None
    def __init__(self, d=None) -> None: ...
