from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrJobFamilyCreatedV2Data:
    job_family_id: str | None
    def __init__(self, d=None) -> None: ...

class P2CorehrJobFamilyCreatedV2(EventContext):
    event: P2CorehrJobFamilyCreatedV2Data | None
    def __init__(self, d=None) -> None: ...
