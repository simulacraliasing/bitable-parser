from .query_metric_template_response_body import QueryMetricTemplateResponseBody as QueryMetricTemplateResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryMetricTemplateResponse(BaseResponse):
    data: QueryMetricTemplateResponseBody | None
    def __init__(self, d=None) -> None: ...
