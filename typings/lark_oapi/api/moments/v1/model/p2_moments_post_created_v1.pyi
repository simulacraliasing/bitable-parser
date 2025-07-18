from .user_id import UserId as UserId
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2MomentsPostCreatedV1Data:
    id: str | None
    user_id: UserId | None
    create_time: str | None
    category_ids: list[str] | None
    link: str | None
    user_type: int | None
    def __init__(self, d=None) -> None: ...

class P2MomentsPostCreatedV1(EventContext):
    event: P2MomentsPostCreatedV1Data | None
    def __init__(self, d=None) -> None: ...
