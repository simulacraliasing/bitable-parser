from .old_user_object import OldUserObject as OldUserObject
from .user_event import UserEvent as UserEvent
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2ContactUserDeletedV3Data:
    object: UserEvent | None
    old_object: OldUserObject | None
    def __init__(self, d=None) -> None: ...

class P2ContactUserDeletedV3(EventContext):
    event: P2ContactUserDeletedV3Data | None
    def __init__(self, d=None) -> None: ...
