from .create_version_cost_allocation_response_body import CreateVersionCostAllocationResponseBody as CreateVersionCostAllocationResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateVersionCostAllocationResponse(BaseResponse):
    data: CreateVersionCostAllocationResponseBody | None
    def __init__(self, d=None) -> None: ...
