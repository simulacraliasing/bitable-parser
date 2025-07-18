from .search_chat_response_body import SearchChatResponseBody as SearchChatResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchChatResponse(BaseResponse):
    data: SearchChatResponseBody | None
    def __init__(self, d=None) -> None: ...
