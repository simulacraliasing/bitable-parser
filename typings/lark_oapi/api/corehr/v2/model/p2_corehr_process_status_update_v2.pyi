from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrProcessStatusUpdateV2Data:
    process_id: str | None
    status: int | None
    biz_type: str | None
    flow_definition_id: str | None
    properties: int | None
    def __init__(self, d=None) -> None: ...

class P2CorehrProcessStatusUpdateV2(EventContext):
    event: P2CorehrProcessStatusUpdateV2Data | None
    def __init__(self, d=None) -> None: ...
