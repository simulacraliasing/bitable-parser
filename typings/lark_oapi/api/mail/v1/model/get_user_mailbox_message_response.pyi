from .get_user_mailbox_message_response_body import GetUserMailboxMessageResponseBody as GetUserMailboxMessageResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetUserMailboxMessageResponse(BaseResponse):
    data: GetUserMailboxMessageResponseBody | None
    def __init__(self, d=None) -> None: ...
