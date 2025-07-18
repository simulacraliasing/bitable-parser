from .get_by_card_user_mailbox_message_response_body import GetByCardUserMailboxMessageResponseBody as GetByCardUserMailboxMessageResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetByCardUserMailboxMessageResponse(BaseResponse):
    data: GetByCardUserMailboxMessageResponseBody | None
    def __init__(self, d=None) -> None: ...
