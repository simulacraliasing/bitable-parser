from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrCostCenterDeletedV2Data:
    cost_center_id: str | None
    def __init__(self, d=None) -> None: ...

class P2CorehrCostCenterDeletedV2(EventContext):
    event: P2CorehrCostCenterDeletedV2Data | None
    def __init__(self, d=None) -> None: ...
