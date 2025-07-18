from .list_cost_allocation_plan_response_body import ListCostAllocationPlanResponseBody as ListCostAllocationPlanResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListCostAllocationPlanResponse(BaseResponse):
    data: ListCostAllocationPlanResponseBody | None
    def __init__(self, d=None) -> None: ...
