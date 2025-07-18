from .create_chat_menu_tree_response_body import CreateChatMenuTreeResponseBody as CreateChatMenuTreeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateChatMenuTreeResponse(BaseResponse):
    data: CreateChatMenuTreeResponseBody | None
    def __init__(self, d=None) -> None: ...
