from .sort_chat_menu_tree_response_body import SortChatMenuTreeResponseBody as SortChatMenuTreeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SortChatMenuTreeResponse(BaseResponse):
    data: SortChatMenuTreeResponseBody | None
    def __init__(self, d=None) -> None: ...
