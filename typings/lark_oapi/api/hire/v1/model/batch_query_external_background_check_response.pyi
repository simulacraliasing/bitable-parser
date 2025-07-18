from .batch_query_external_background_check_response_body import BatchQueryExternalBackgroundCheckResponseBody as BatchQueryExternalBackgroundCheckResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchQueryExternalBackgroundCheckResponse(BaseResponse):
    data: BatchQueryExternalBackgroundCheckResponseBody | None
    def __init__(self, d=None) -> None: ...
