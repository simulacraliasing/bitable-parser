from .adjustment_logic import AdjustmentLogic as AdjustmentLogic
from lark_oapi.core.construct import init as init

class PlanItem:
    adjustment_type: str | None
    item_id: str | None
    plan_item_logic: AdjustmentLogic | None
    probation_discount_type: str | None
    probation_discount_percentum: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> PlanItemBuilder: ...

class PlanItemBuilder:
    def __init__(self) -> None: ...
    def adjustment_type(self, adjustment_type: str) -> PlanItemBuilder: ...
    def item_id(self, item_id: str) -> PlanItemBuilder: ...
    def plan_item_logic(self, plan_item_logic: AdjustmentLogic) -> PlanItemBuilder: ...
    def probation_discount_type(self, probation_discount_type: str) -> PlanItemBuilder: ...
    def probation_discount_percentum(self, probation_discount_percentum: str) -> PlanItemBuilder: ...
    def build(self) -> PlanItem: ...
