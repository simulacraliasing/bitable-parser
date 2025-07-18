from .create_message_reaction_response_body import CreateMessageReactionResponseBody as CreateMessageReactionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateMessageReactionResponse(BaseResponse):
    data: CreateMessageReactionResponseBody | None
    def __init__(self, d=None) -> None: ...
