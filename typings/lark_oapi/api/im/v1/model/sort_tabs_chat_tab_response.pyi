from .sort_tabs_chat_tab_response_body import SortTabsChatTabResponseBody as SortTabsChatTabResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SortTabsChatTabResponse(BaseResponse):
    data: SortTabsChatTabResponseBody | None
    def __init__(self, d=None) -> None: ...
