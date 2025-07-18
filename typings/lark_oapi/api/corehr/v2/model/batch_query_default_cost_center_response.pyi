from .batch_query_default_cost_center_response_body import BatchQueryDefaultCostCenterResponseBody as BatchQueryDefaultCostCenterResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchQueryDefaultCostCenterResponse(BaseResponse):
    data: BatchQueryDefaultCostCenterResponseBody | None
    def __init__(self, d=None) -> None: ...
