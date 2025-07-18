from .list_message_reaction_response_body import ListMessageReactionResponseBody as ListMessageReactionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListMessageReactionResponse(BaseResponse):
    data: ListMessageReactionResponseBody | None
    def __init__(self, d=None) -> None: ...
