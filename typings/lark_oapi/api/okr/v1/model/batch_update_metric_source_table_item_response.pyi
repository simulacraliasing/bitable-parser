from .batch_update_metric_source_table_item_response_body import BatchUpdateMetricSourceTableItemResponseBody as BatchUpdateMetricSourceTableItemResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchUpdateMetricSourceTableItemResponse(BaseResponse):
    data: BatchUpdateMetricSourceTableItemResponseBody | None
    def __init__(self, d=None) -> None: ...
