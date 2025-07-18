from .patch_period_response_body import PatchPeriodResponseBody as PatchPeriodResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchPeriodResponse(BaseResponse):
    data: PatchPeriodResponseBody | None
    def __init__(self, d=None) -> None: ...
