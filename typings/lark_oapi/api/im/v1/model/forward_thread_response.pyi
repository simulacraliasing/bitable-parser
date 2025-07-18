from .forward_thread_response_body import ForwardThreadResponseBody as ForwardThreadResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ForwardThreadResponse(BaseResponse):
    data: ForwardThreadResponseBody | None
    def __init__(self, d=None) -> None: ...
