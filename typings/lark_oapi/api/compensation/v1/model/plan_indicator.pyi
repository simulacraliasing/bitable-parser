from .adjustment_logic import AdjustmentLogic as AdjustmentLogic
from lark_oapi.core.construct import init as init

class PlanIndicator:
    indicator_id: str | None
    plan_indicator_logic: AdjustmentLogic | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> PlanIndicatorBuilder: ...

class PlanIndicatorBuilder:
    def __init__(self) -> None: ...
    def indicator_id(self, indicator_id: str) -> PlanIndicatorBuilder: ...
    def plan_indicator_logic(self, plan_indicator_logic: AdjustmentLogic) -> PlanIndicatorBuilder: ...
    def build(self) -> PlanIndicator: ...
