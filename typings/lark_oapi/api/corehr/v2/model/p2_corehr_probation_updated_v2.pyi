from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrProbationUpdatedV2Data:
    employment_id: str | None
    probation_status: str | None
    actual_probation_end_date: str | None
    def __init__(self, d=None) -> None: ...

class P2CorehrProbationUpdatedV2(EventContext):
    event: P2CorehrProbationUpdatedV2Data | None
    def __init__(self, d=None) -> None: ...
