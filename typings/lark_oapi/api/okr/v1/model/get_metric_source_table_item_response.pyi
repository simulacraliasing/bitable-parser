from .get_metric_source_table_item_response_body import GetMetricSourceTableItemResponseBody as GetMetricSourceTableItemResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetMetricSourceTableItemResponse(BaseResponse):
    data: GetMetricSourceTableItemResponseBody | None
    def __init__(self, d=None) -> None: ...
