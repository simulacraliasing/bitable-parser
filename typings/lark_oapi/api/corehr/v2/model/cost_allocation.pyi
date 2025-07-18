from .job_data_cost_center import JobDataCostCenter as JobDataCostCenter
from lark_oapi.core.construct import init as init

class CostAllocation:
    effective_time: str | None
    expiration_time: str | None
    cost_center_rates: list[JobDataCostCenter] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CostAllocationBuilder: ...

class CostAllocationBuilder:
    def __init__(self) -> None: ...
    def effective_time(self, effective_time: str) -> CostAllocationBuilder: ...
    def expiration_time(self, expiration_time: str) -> CostAllocationBuilder: ...
    def cost_center_rates(self, cost_center_rates: list[JobDataCostCenter]) -> CostAllocationBuilder: ...
    def build(self) -> CostAllocation: ...
