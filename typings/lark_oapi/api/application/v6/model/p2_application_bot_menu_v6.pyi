from .operator import Operator as Operator
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2ApplicationBotMenuV6Data:
    operator: Operator | None
    event_key: str | None
    timestamp: int | None
    def __init__(self, d=None) -> None: ...

class P2ApplicationBotMenuV6(EventContext):
    event: P2ApplicationBotMenuV6Data | None
    def __init__(self, d=None) -> None: ...
