from typing import *
from .context import EventContext as EventContext
from .processor import IEventProcessor as IEventProcessor
from _typeshed import Incomplete
from lark_oapi.core.construct import init as init

class CustomizedEvent(EventContext):
    event: Optional[Dict]
    def __init__(self, d=None) -> None: ...

class CustomizedEventProcessor(IEventProcessor[CustomizedEvent]):
    f: Incomplete
    def __init__(self, f: Callable[[CustomizedEvent], None]) -> None: ...
    def type(self) -> Type[CustomizedEvent]: ...
    def do(self, data: CustomizedEvent) -> None: ...
