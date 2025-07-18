from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrJobGradeCreatedV2Data:
    job_grade_id: str | None
    def __init__(self, d=None) -> None: ...

class P2CorehrJobGradeCreatedV2(EventContext):
    event: P2CorehrJobGradeCreatedV2Data | None
    def __init__(self, d=None) -> None: ...
