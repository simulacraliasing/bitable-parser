from .delete_chat_menu_tree_response_body import DeleteChatMenuTreeResponseBody as DeleteChatMenuTreeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class DeleteChatMenuTreeResponse(BaseResponse):
    data: DeleteChatMenuTreeResponseBody | None
    def __init__(self, d=None) -> None: ...
