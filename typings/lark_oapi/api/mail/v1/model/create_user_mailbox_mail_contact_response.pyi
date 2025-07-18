from .create_user_mailbox_mail_contact_response_body import CreateUserMailboxMailContactResponseBody as CreateUserMailboxMailContactResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateUserMailboxMailContactResponse(BaseResponse):
    data: CreateUserMailboxMailContactResponseBody | None
    def __init__(self, d=None) -> None: ...
