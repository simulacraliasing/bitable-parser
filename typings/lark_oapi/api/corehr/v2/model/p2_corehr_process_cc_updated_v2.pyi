from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrProcessCcUpdatedV2Data:
    process_id: str | None
    approver_id: str | None
    status: int | None
    biz_type: str | None
    def __init__(self, d=None) -> None: ...

class P2CorehrProcessCcUpdatedV2(EventContext):
    event: P2CorehrProcessCcUpdatedV2Data | None
    def __init__(self, d=None) -> None: ...
