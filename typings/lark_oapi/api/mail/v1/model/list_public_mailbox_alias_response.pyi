from .list_public_mailbox_alias_response_body import ListPublicMailboxAliasResponseBody as ListPublicMailboxAliasResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListPublicMailboxAliasResponse(BaseResponse):
    data: ListPublicMailboxAliasResponseBody | None
    def __init__(self, d=None) -> None: ...
