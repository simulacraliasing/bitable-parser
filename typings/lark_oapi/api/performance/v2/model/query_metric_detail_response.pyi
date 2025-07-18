from .query_metric_detail_response_body import QueryMetricDetailResponseBody as QueryMetricDetailResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryMetricDetailResponse(BaseResponse):
    data: QueryMetricDetailResponseBody | None
    def __init__(self, d=None) -> None: ...
