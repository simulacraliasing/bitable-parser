from .batch_workforce_plan_detail_response_body import BatchWorkforcePlanDetailResponseBody as BatchWorkforcePlanDetailResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchWorkforcePlanDetailResponse(BaseResponse):
    data: BatchWorkforcePlanDetailResponseBody | None
    def __init__(self, d=None) -> None: ...
