from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrJobDataDeletedV1Data:
    job_data_id: str | None
    def __init__(self, d=None) -> None: ...

class P2CorehrJobDataDeletedV1(EventContext):
    event: P2CorehrJobDataDeletedV1Data | None
    def __init__(self, d=None) -> None: ...
