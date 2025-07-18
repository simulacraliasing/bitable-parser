from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrJobLevelUpdatedV2Data:
    job_level_id: str | None
    field_changes: list[str] | None
    def __init__(self, d=None) -> None: ...

class P2CorehrJobLevelUpdatedV2(EventContext):
    event: P2CorehrJobLevelUpdatedV2Data | None
    def __init__(self, d=None) -> None: ...
