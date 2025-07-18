from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrJobLevelCreatedV2Data:
    job_level_id: str | None
    def __init__(self, d=None) -> None: ...

class P2CorehrJobLevelCreatedV2(EventContext):
    event: P2CorehrJobLevelCreatedV2Data | None
    def __init__(self, d=None) -> None: ...
