from .model.p2_approval_approval_updated_v4 import P2ApprovalApprovalUpdatedV4 as P2ApprovalApprovalUpdatedV4
from _typeshed import Incomplete
from lark_oapi.event.processor import IEventProcessor as IEventProcessor
from typing import Callable

class P2ApprovalApprovalUpdatedV4Processor(IEventProcessor[P2ApprovalApprovalUpdatedV4]):
    f: Incomplete
    def __init__(self, f: Callable[[P2ApprovalApprovalUpdatedV4], None]) -> None: ...
    def type(self) -> type[P2ApprovalApprovalUpdatedV4]: ...
    def do(self, data: P2ApprovalApprovalUpdatedV4) -> None: ...
