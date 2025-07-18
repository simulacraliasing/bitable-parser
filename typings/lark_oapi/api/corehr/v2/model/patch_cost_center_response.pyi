from .patch_cost_center_response_body import PatchCostCenterResponseBody as PatchCostCenterResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchCostCenterResponse(BaseResponse):
    data: PatchCostCenterResponseBody | None
    def __init__(self, d=None) -> None: ...
