from .user_id import UserId as UserId
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2MomentsDislikeDeletedV1Data:
    entity_type: int | None
    entity_id: str | None
    user_id: UserId | None
    id: str | None
    def __init__(self, d=None) -> None: ...

class P2MomentsDislikeDeletedV1(EventContext):
    event: P2MomentsDislikeDeletedV1Data | None
    def __init__(self, d=None) -> None: ...
