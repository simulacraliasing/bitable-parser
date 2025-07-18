from .open_result import OpenResult as OpenResult
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2PerformanceStageTaskOpenResultV2Data:
    items: list[OpenResult] | None
    def __init__(self, d=None) -> None: ...

class P2PerformanceStageTaskOpenResultV2(EventContext):
    event: P2PerformanceStageTaskOpenResultV2Data | None
    def __init__(self, d=None) -> None: ...
