from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrApprovalGroupsUpdatedV2Data:
    approval_group_id: str | None
    process_id: str | None
    approval_group_status: int | None
    topic: str | None
    adjust_reason: str | None
    effective_date: str | None
    created_by: str | None
    draft_id: str | None
    draft_status: int | None
    approval_group_status_v2: int | None
    def __init__(self, d=None) -> None: ...

class P2CorehrApprovalGroupsUpdatedV2(EventContext):
    event: P2CorehrApprovalGroupsUpdatedV2Data | None
    def __init__(self, d=None) -> None: ...
