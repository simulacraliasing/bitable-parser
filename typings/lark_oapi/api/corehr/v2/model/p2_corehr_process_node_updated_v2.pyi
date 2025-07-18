from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrProcessNodeUpdatedV2Data:
    flow_definition_id: str | None
    node_definition_id: str | None
    process_id: str | None
    process_node_id: str | None
    node_type: int | None
    node_status: int | None
    biz_type: str | None
    def __init__(self, d=None) -> None: ...

class P2CorehrProcessNodeUpdatedV2(EventContext):
    event: P2CorehrProcessNodeUpdatedV2Data | None
    def __init__(self, d=None) -> None: ...
