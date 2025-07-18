from .delete_message_reaction_response_body import DeleteMessageReactionResponseBody as DeleteMessageReactionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class DeleteMessageReactionResponse(BaseResponse):
    data: DeleteMessageReactionResponseBody | None
    def __init__(self, d=None) -> None: ...
