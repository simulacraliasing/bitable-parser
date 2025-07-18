from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrCustomOrgDeletedV2Data:
    org_id: str | None
    object_api_name: str | None
    def __init__(self, d=None) -> None: ...

class P2CorehrCustomOrgDeletedV2(EventContext):
    event: P2CorehrCustomOrgDeletedV2Data | None
    def __init__(self, d=None) -> None: ...
