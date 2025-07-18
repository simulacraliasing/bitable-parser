from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrJobDataUpdatedV1Data:
    job_data_id: str | None
    def __init__(self, d=None) -> None: ...

class P2CorehrJobDataUpdatedV1(EventContext):
    event: P2CorehrJobDataUpdatedV1Data | None
    def __init__(self, d=None) -> None: ...
