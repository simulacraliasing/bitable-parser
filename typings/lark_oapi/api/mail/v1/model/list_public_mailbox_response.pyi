from .list_public_mailbox_response_body import ListPublicMailboxResponseBody as ListPublicMailboxResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListPublicMailboxResponse(BaseResponse):
    data: ListPublicMailboxResponseBody | None
    def __init__(self, d=None) -> None: ...
