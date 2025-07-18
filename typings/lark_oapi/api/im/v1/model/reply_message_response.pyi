from .reply_message_response_body import ReplyMessageResponseBody as ReplyMessageResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ReplyMessageResponse(BaseResponse):
    data: ReplyMessageResponseBody | None
    def __init__(self, d=None) -> None: ...
