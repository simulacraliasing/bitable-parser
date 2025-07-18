from .patch_cost_center_version_response_body import PatchCostCenterVersionResponseBody as PatchCostCenterVersionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchCostCenterVersionResponse(BaseResponse):
    data: PatchCostCenterVersionResponseBody | None
    def __init__(self, d=None) -> None: ...
