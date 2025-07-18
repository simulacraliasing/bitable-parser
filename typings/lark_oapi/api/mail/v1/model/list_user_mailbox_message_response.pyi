from .list_user_mailbox_message_response_body import ListUserMailboxMessageResponseBody as ListUserMailboxMessageResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListUserMailboxMessageResponse(BaseResponse):
    data: ListUserMailboxMessageResponseBody | None
    def __init__(self, d=None) -> None: ...
