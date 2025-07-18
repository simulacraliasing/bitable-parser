from .batch_close_system_status_response_body import BatchCloseSystemStatusResponseBody as BatchCloseSystemStatusResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchCloseSystemStatusResponse(BaseResponse):
    data: BatchCloseSystemStatusResponseBody | None
    def __init__(self, d=None) -> None: ...
