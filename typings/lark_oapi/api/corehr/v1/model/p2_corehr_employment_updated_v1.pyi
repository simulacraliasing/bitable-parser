from .user_id import UserId as UserId
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrEmploymentUpdatedV1Data:
    employment_id: str | None
    target_user_id: UserId | None
    field_changes: list[str] | None
    def __init__(self, d=None) -> None: ...

class P2CorehrEmploymentUpdatedV1(EventContext):
    event: P2CorehrEmploymentUpdatedV1Data | None
    def __init__(self, d=None) -> None: ...
