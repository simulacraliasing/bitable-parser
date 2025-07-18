from .approval_config_event import ApprovalConfigEvent as ApprovalConfigEvent
from .reserve_scope_config_event import ReserveScopeConfigEvent as ReserveScopeConfigEvent
from .time_config import TimeConfig as TimeConfig
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2VcReserveConfigUpdatedV1Data:
    scope_id: str | None
    scope_type: int | None
    approve_config: ApprovalConfigEvent | None
    time_config: TimeConfig | None
    reserve_scope_config: ReserveScopeConfigEvent | None
    def __init__(self, d=None) -> None: ...

class P2VcReserveConfigUpdatedV1(EventContext):
    event: P2VcReserveConfigUpdatedV1Data | None
    def __init__(self, d=None) -> None: ...
