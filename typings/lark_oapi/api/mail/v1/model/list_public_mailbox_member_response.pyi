from .list_public_mailbox_member_response_body import ListPublicMailboxMemberResponseBody as ListPublicMailboxMemberResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListPublicMailboxMemberResponse(BaseResponse):
    data: ListPublicMailboxMemberResponseBody | None
    def __init__(self, d=None) -> None: ...
