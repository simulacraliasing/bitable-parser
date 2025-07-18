from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrCostCenterUpdatedV2Data:
    cost_center_id: str | None
    field_changes: list[str] | None
    def __init__(self, d=None) -> None: ...

class P2CorehrCostCenterUpdatedV2(EventContext):
    event: P2CorehrCostCenterUpdatedV2Data | None
    def __init__(self, d=None) -> None: ...
