from .create_chat_tab_response_body import CreateChatTabResponseBody as CreateChatTabResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateChatTabResponse(BaseResponse):
    data: CreateChatTabResponseBody | None
    def __init__(self, d=None) -> None: ...
