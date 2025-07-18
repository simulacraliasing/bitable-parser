from .list_user_mailbox_mail_contact_response_body import ListUserMailboxMailContactResponseBody as ListUserMailboxMailContactResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListUserMailboxMailContactResponse(BaseResponse):
    data: ListUserMailboxMailContactResponseBody | None
    def __init__(self, d=None) -> None: ...
