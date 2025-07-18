from .employment_cost_allocation import EmploymentCostAllocation as EmploymentCostAllocation
from lark_oapi.core.construct import init as init

class UpdateVersionCostAllocationRequestBody:
    employment_id: str | None
    cost_allocation: EmploymentCostAllocation | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> UpdateVersionCostAllocationRequestBodyBuilder: ...

class UpdateVersionCostAllocationRequestBodyBuilder:
    def __init__(self) -> None: ...
    def employment_id(self, employment_id: str) -> UpdateVersionCostAllocationRequestBodyBuilder: ...
    def cost_allocation(self, cost_allocation: EmploymentCostAllocation) -> UpdateVersionCostAllocationRequestBodyBuilder: ...
    def build(self) -> UpdateVersionCostAllocationRequestBody: ...
