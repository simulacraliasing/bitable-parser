from .user import User as User
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2ApplicationApplicationVisibilityAddedV6Data:
    users: list[User] | None
    source: int | None
    def __init__(self, d=None) -> None: ...

class P2ApplicationApplicationVisibilityAddedV6(EventContext):
    event: P2ApplicationApplicationVisibilityAddedV6Data | None
    def __init__(self, d=None) -> None: ...
