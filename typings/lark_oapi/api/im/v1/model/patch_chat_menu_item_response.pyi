from .patch_chat_menu_item_response_body import PatchChatMenuItemResponseBody as PatchChatMenuItemResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchChatMenuItemResponse(BaseResponse):
    data: PatchChatMenuItemResponseBody | None
    def __init__(self, d=None) -> None: ...
