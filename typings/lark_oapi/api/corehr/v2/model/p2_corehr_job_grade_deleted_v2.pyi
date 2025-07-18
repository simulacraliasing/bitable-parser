from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrJobGradeDeletedV2Data:
    job_grade_id: str | None
    def __init__(self, d=None) -> None: ...

class P2CorehrJobGradeDeletedV2(EventContext):
    event: P2CorehrJobGradeDeletedV2Data | None
    def __init__(self, d=None) -> None: ...
