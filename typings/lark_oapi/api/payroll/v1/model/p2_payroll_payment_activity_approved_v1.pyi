from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2PayrollPaymentActivityApprovedV1Data:
    activity_id: str | None
    def __init__(self, d=None) -> None: ...

class P2PayrollPaymentActivityApprovedV1(EventContext):
    event: P2PayrollPaymentActivityApprovedV1Data | None
    def __init__(self, d=None) -> None: ...
