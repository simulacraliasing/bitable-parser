from .list_metric_source_table_response_body import ListMetricSourceTableResponseBody as ListMetricSourceTableResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListMetricSourceTableResponse(BaseResponse):
    data: ListMetricSourceTableResponseBody | None
    def __init__(self, d=None) -> None: ...
