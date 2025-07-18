from .user_id import UserId as UserId
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2AcsUserUpdatedV1Data:
    user_id: UserId | None
    card: int | None
    face_uploaded: bool | None
    def __init__(self, d=None) -> None: ...

class P2AcsUserUpdatedV1(EventContext):
    event: P2AcsUserUpdatedV1Data | None
    def __init__(self, d=None) -> None: ...
