from .get_public_mailbox_member_response_body import GetPublicMailboxMemberResponseBody as GetPublicMailboxMemberResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetPublicMailboxMemberResponse(BaseResponse):
    data: GetPublicMailboxMemberResponseBody | None
    def __init__(self, d=None) -> None: ...
