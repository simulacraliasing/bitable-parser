from .user_id_list import UserIdList as UserIdList
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2TaskTaskUpdateTenantV1Data:
    user_id_list: UserIdList | None
    task_id: str | None
    object_type: str | None
    event_type: str | None
    def __init__(self, d=None) -> None: ...

class P2TaskTaskUpdateTenantV1(EventContext):
    event: P2TaskTaskUpdateTenantV1Data | None
    def __init__(self, d=None) -> None: ...
