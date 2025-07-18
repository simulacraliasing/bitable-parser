from .query_metric_lib_response_body import QueryMetricLibResponseBody as QueryMetricLibResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryMetricLibResponse(BaseResponse):
    data: QueryMetricLibResponseBody | None
    def __init__(self, d=None) -> None: ...
