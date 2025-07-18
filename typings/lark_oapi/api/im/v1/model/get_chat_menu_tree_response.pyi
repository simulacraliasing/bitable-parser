from .get_chat_menu_tree_response_body import GetChatMenuTreeResponseBody as GetChatMenuTreeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetChatMenuTreeResponse(BaseResponse):
    data: GetChatMenuTreeResponseBody | None
    def __init__(self, d=None) -> None: ...
