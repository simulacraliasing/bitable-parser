from .update_chat_button_response_body import UpdateChatButtonResponseBody as UpdateChatButtonResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdateChatButtonResponse(BaseResponse):
    data: UpdateChatButtonResponseBody | None
    def __init__(self, d=None) -> None: ...
