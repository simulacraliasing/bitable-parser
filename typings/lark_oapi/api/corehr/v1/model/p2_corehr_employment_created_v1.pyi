from .user_id import UserId as UserId
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrEmploymentCreatedV1Data:
    employment_id: str | None
    target_user_id: UserId | None
    def __init__(self, d=None) -> None: ...

class P2CorehrEmploymentCreatedV1(EventContext):
    event: P2CorehrEmploymentCreatedV1Data | None
    def __init__(self, d=None) -> None: ...
