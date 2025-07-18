from .list_user_mailbox_alias_response_body import ListUserMailboxAliasResponseBody as ListUserMailboxAliasResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListUserMailboxAliasResponse(BaseResponse):
    data: ListUserMailboxAliasResponseBody | None
    def __init__(self, d=None) -> None: ...
