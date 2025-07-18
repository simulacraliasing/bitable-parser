from .user_id import UserId as UserId
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2MomentsReactionCreatedV1Data:
    type: str | None
    user_id: UserId | None
    entity_id: str | None
    id: str | None
    entity_type: int | None
    user_type: int | None
    create_time: str | None
    def __init__(self, d=None) -> None: ...

class P2MomentsReactionCreatedV1(EventContext):
    event: P2MomentsReactionCreatedV1Data | None
    def __init__(self, d=None) -> None: ...
