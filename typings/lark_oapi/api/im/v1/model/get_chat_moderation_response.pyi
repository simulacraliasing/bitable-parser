from .get_chat_moderation_response_body import GetChatModerationResponseBody as GetChatModerationResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetChatModerationResponse(BaseResponse):
    data: GetChatModerationResponseBody | None
    def __init__(self, d=None) -> None: ...
