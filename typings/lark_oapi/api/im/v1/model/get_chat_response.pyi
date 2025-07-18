from .get_chat_response_body import GetChatResponseBody as GetChatResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetChatResponse(BaseResponse):
    data: GetChatResponseBody | None
    def __init__(self, d=None) -> None: ...
