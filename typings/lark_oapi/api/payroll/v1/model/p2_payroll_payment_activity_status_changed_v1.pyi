from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2PayrollPaymentActivityStatusChangedV1Data:
    activity_id: int | None
    status: int | None
    def __init__(self, d=None) -> None: ...

class P2PayrollPaymentActivityStatusChangedV1(EventContext):
    event: P2PayrollPaymentActivityStatusChangedV1Data | None
    def __init__(self, d=None) -> None: ...
