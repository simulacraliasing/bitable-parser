from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrJobDataCreatedV1Data:
    job_data_id: str | None
    def __init__(self, d=None) -> None: ...

class P2CorehrJobDataCreatedV1(EventContext):
    event: P2CorehrJobDataCreatedV1Data | None
    def __init__(self, d=None) -> None: ...
