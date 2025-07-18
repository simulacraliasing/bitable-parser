from .dimension_entity import DimensionEntity as DimensionEntity
from .workforce_plan_eai_detail import WorkforcePlanEaiDetail as WorkforcePlanEaiDetail
from .workforce_plan_multi_period_value import WorkforcePlanMultiPeriodValue as WorkforcePlanMultiPeriodValue
from lark_oapi.core.construct import init as init

class WorkforcePlanDetailRow:
    dimensions: list[DimensionEntity] | None
    eai_details: list[WorkforcePlanEaiDetail] | None
    plan_value: str | None
    multi_period_values: list[WorkforcePlanMultiPeriodValue] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> WorkforcePlanDetailRowBuilder: ...

class WorkforcePlanDetailRowBuilder:
    def __init__(self) -> None: ...
    def dimensions(self, dimensions: list[DimensionEntity]) -> WorkforcePlanDetailRowBuilder: ...
    def eai_details(self, eai_details: list[WorkforcePlanEaiDetail]) -> WorkforcePlanDetailRowBuilder: ...
    def plan_value(self, plan_value: str) -> WorkforcePlanDetailRowBuilder: ...
    def multi_period_values(self, multi_period_values: list[WorkforcePlanMultiPeriodValue]) -> WorkforcePlanDetailRowBuilder: ...
    def build(self) -> WorkforcePlanDetailRow: ...
