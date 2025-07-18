from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrCustomOrgUpdatedV2Data:
    org_id: str | None
    field_changes: list[str] | None
    object_api_name: str | None
    def __init__(self, d=None) -> None: ...

class P2CorehrCustomOrgUpdatedV2(EventContext):
    event: P2CorehrCustomOrgUpdatedV2Data | None
    def __init__(self, d=None) -> None: ...
