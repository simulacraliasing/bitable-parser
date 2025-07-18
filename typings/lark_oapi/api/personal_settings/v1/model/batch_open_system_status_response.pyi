from .batch_open_system_status_response_body import BatchOpenSystemStatusResponseBody as BatchOpenSystemStatusResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchOpenSystemStatusResponse(BaseResponse):
    data: BatchOpenSystemStatusResponseBody | None
    def __init__(self, d=None) -> None: ...
