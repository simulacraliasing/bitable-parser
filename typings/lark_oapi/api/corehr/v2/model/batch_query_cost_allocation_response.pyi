from .batch_query_cost_allocation_response_body import BatchQueryCostAllocationResponseBody as BatchQueryCostAllocationResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchQueryCostAllocationResponse(BaseResponse):
    data: BatchQueryCostAllocationResponseBody | None
    def __init__(self, d=None) -> None: ...
