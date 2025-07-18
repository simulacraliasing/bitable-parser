from .list_chat_response_body import ListChatResponseBody as ListChatResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListChatResponse(BaseResponse):
    data: ListChatResponseBody | None
    def __init__(self, d=None) -> None: ...
