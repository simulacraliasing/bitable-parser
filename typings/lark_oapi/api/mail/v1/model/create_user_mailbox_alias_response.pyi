from .create_user_mailbox_alias_response_body import CreateUserMailboxAliasResponseBody as CreateUserMailboxAliasResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateUserMailboxAliasResponse(BaseResponse):
    data: CreateUserMailboxAliasResponseBody | None
    def __init__(self, d=None) -> None: ...
