from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrJobFamilyDeletedV2Data:
    job_family_id: str | None
    def __init__(self, d=None) -> None: ...

class P2CorehrJobFamilyDeletedV2(EventContext):
    event: P2CorehrJobFamilyDeletedV2Data | None
    def __init__(self, d=None) -> None: ...
