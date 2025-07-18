from .batch_get_location_response_body import BatchGetLocationResponseBody as BatchGetLocationResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchGetLocationResponse(BaseResponse):
    data: BatchGetLocationResponseBody | None
    def __init__(self, d=None) -> None: ...
