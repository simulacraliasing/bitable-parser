from .scope import Scope as Scope
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2ContactScopeUpdatedV3Data:
    added: Scope | None
    removed: Scope | None
    def __init__(self, d=None) -> None: ...

class P2ContactScopeUpdatedV3(EventContext):
    event: P2ContactScopeUpdatedV3Data | None
    def __init__(self, d=None) -> None: ...
