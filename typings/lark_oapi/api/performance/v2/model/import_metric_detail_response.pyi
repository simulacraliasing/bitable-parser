from .import_metric_detail_response_body import ImportMetricDetailResponseBody as ImportMetricDetailResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ImportMetricDetailResponse(BaseResponse):
    data: ImportMetricDetailResponseBody | None
    def __init__(self, d=None) -> None: ...
