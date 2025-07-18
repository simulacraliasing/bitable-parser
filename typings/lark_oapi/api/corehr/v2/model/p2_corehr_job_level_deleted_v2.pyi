from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrJobLevelDeletedV2Data:
    job_level_id: str | None
    def __init__(self, d=None) -> None: ...

class P2CorehrJobLevelDeletedV2(EventContext):
    event: P2CorehrJobLevelDeletedV2Data | None
    def __init__(self, d=None) -> None: ...
