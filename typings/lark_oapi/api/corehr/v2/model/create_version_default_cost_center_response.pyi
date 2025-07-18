from .create_version_default_cost_center_response_body import CreateVersionDefaultCostCenterResponseBody as CreateVersionDefaultCostCenterResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateVersionDefaultCostCenterResponse(BaseResponse):
    data: CreateVersionDefaultCostCenterResponseBody | None
    def __init__(self, d=None) -> None: ...
