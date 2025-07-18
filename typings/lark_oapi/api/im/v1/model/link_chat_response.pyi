from .link_chat_response_body import LinkChatResponseBody as LinkChatResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class LinkChatResponse(BaseResponse):
    data: LinkChatResponseBody | None
    def __init__(self, d=None) -> None: ...
