from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrProcessApproverUpdatedV2Data:
    process_id: str | None
    approver_id: str | None
    type: int | None
    status: int | None
    biz_type: str | None
    flow_definition_id: str | None
    node_definition_id: str | None
    node_id: str | None
    def __init__(self, d=None) -> None: ...

class P2CorehrProcessApproverUpdatedV2(EventContext):
    event: P2CorehrProcessApproverUpdatedV2Data | None
    def __init__(self, d=None) -> None: ...
