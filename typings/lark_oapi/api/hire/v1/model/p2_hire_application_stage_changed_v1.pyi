from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2HireApplicationStageChangedV1Data:
    application_id: str | None
    origin_stage_id: str | None
    target_stage_id: str | None
    update_time: int | None
    def __init__(self, d=None) -> None: ...

class P2HireApplicationStageChangedV1(EventContext):
    event: P2HireApplicationStageChangedV1Data | None
    def __init__(self, d=None) -> None: ...
