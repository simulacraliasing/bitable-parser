from .query_metric_field_response_body import QueryMetricFieldResponseBody as QueryMetricFieldResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryMetricFieldResponse(BaseResponse):
    data: QueryMetricFieldResponseBody | None
    def __init__(self, d=None) -> None: ...
