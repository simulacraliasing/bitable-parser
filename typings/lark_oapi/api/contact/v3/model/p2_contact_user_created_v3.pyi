from .user_event import UserEvent as UserEvent
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2ContactUserCreatedV3Data:
    object: UserEvent | None
    def __init__(self, d=None) -> None: ...

class P2ContactUserCreatedV3(EventContext):
    event: P2ContactUserCreatedV3Data | None
    def __init__(self, d=None) -> None: ...
