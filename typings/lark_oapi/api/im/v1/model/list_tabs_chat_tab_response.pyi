from .list_tabs_chat_tab_response_body import ListTabsChatTabResponseBody as ListTabsChatTabResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListTabsChatTabResponse(BaseResponse):
    data: ListTabsChatTabResponseBody | None
    def __init__(self, d=None) -> None: ...
