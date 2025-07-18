from .user_id import UserId as UserId
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrJobDataChangedV1Data:
    job_data_id: str | None
    employment_id: str | None
    target_user_id: UserId | None
    job_change_id: str | None
    def __init__(self, d=None) -> None: ...

class P2CorehrJobDataChangedV1(EventContext):
    event: P2CorehrJobDataChangedV1Data | None
    def __init__(self, d=None) -> None: ...
