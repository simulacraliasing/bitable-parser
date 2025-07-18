from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrJobFamilyUpdatedV2Data:
    job_family_id: str | None
    field_changes: list[str] | None
    def __init__(self, d=None) -> None: ...

class P2CorehrJobFamilyUpdatedV2(EventContext):
    event: P2CorehrJobFamilyUpdatedV2Data | None
    def __init__(self, d=None) -> None: ...
