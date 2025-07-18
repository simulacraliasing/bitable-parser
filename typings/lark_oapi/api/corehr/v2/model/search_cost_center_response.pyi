from .search_cost_center_response_body import SearchCostCenterResponseBody as SearchCostCenterResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchCostCenterResponse(BaseResponse):
    data: SearchCostCenterResponseBody | None
    def __init__(self, d=None) -> None: ...
