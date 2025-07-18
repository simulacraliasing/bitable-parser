from .approval_event import ApprovalEvent as ApprovalEvent
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2ApprovalApprovalUpdatedV4Data:
    object: ApprovalEvent | None
    def __init__(self, d=None) -> None: ...

class P2ApprovalApprovalUpdatedV4(EventContext):
    event: P2ApprovalApprovalUpdatedV4Data | None
    def __init__(self, d=None) -> None: ...
