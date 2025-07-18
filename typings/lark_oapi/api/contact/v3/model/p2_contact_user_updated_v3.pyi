from .user_event import UserEvent as UserEvent
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2ContactUserUpdatedV3Data:
    object: UserEvent | None
    old_object: UserEvent | None
    def __init__(self, d=None) -> None: ...

class P2ContactUserUpdatedV3(EventContext):
    event: P2ContactUserUpdatedV3Data | None
    def __init__(self, d=None) -> None: ...
