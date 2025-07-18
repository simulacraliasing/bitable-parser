from lark_oapi.core.construct import init as init

class CreateVersionCostAllocationResponseBody:
    cost_allocation_id: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CreateVersionCostAllocationResponseBodyBuilder: ...

class CreateVersionCostAllocationResponseBodyBuilder:
    def __init__(self) -> None: ...
    def cost_allocation_id(self, cost_allocation_id: str) -> CreateVersionCostAllocationResponseBodyBuilder: ...
    def build(self) -> CreateVersionCostAllocationResponseBody: ...
