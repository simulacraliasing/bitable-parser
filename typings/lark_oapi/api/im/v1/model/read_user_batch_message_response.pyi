from .read_user_batch_message_response_body import ReadUserBatchMessageResponseBody as ReadUserBatchMessageResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ReadUserBatchMessageResponse(BaseResponse):
    data: ReadUserBatchMessageResponseBody | None
    def __init__(self, d=None) -> None: ...
