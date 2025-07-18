from .patch_metric_source_table_item_response_body import PatchMetricSourceTableItemResponseBody as PatchMetricSourceTableItemResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchMetricSourceTableItemResponse(BaseResponse):
    data: PatchMetricSourceTableItemResponseBody | None
    def __init__(self, d=None) -> None: ...
