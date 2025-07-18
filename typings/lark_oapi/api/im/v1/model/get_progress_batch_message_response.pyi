from .get_progress_batch_message_response_body import GetProgressBatchMessageResponseBody as GetProgressBatchMessageResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetProgressBatchMessageResponse(BaseResponse):
    data: GetProgressBatchMessageResponseBody | None
    def __init__(self, d=None) -> None: ...
