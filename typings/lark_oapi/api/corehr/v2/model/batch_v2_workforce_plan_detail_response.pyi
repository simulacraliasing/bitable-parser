from .batch_v2_workforce_plan_detail_response_body import BatchV2WorkforcePlanDetailResponseBody as BatchV2WorkforcePlanDetailResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchV2WorkforcePlanDetailResponse(BaseResponse):
    data: BatchV2WorkforcePlanDetailResponseBody | None
    def __init__(self, d=None) -> None: ...
