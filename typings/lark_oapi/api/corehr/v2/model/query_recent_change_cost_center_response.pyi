from .query_recent_change_cost_center_response_body import QueryRecentChangeCostCenterResponseBody as QueryRecentChangeCostCenterResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryRecentChangeCostCenterResponse(BaseResponse):
    data: QueryRecentChangeCostCenterResponseBody | None
    def __init__(self, d=None) -> None: ...
