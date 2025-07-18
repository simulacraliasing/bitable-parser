from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrJobCreatedV1Data:
    job_id: str | None
    def __init__(self, d=None) -> None: ...

class P2CorehrJobCreatedV1(EventContext):
    event: P2CorehrJobCreatedV1Data | None
    def __init__(self, d=None) -> None: ...
