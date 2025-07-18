from .create_cost_center_response_body import CreateCostCenterResponseBody as CreateCostCenterResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateCostCenterResponse(BaseResponse):
    data: CreateCostCenterResponseBody | None
    def __init__(self, d=None) -> None: ...
