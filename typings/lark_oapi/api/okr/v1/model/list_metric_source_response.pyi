from .list_metric_source_response_body import ListMetricSourceResponseBody as ListMetricSourceResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListMetricSourceResponse(BaseResponse):
    data: ListMetricSourceResponseBody | None
    def __init__(self, d=None) -> None: ...
