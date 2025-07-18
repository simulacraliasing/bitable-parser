from .list_metric_tag_response_body import ListMetricTagResponseBody as ListMetricTagResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListMetricTagResponse(BaseResponse):
    data: ListMetricTagResponseBody | None
    def __init__(self, d=None) -> None: ...
