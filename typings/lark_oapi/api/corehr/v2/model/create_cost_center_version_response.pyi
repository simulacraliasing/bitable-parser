from .create_cost_center_version_response_body import CreateCostCenterVersionResponseBody as CreateCostCenterVersionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateCostCenterVersionResponse(BaseResponse):
    data: CreateCostCenterVersionResponseBody | None
    def __init__(self, d=None) -> None: ...
