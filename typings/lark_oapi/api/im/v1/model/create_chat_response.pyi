from .create_chat_response_body import CreateChatResponseBody as CreateChatResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateChatResponse(BaseResponse):
    data: CreateChatResponseBody | None
    def __init__(self, d=None) -> None: ...
