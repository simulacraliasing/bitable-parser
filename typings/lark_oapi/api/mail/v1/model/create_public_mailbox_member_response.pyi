from .create_public_mailbox_member_response_body import CreatePublicMailboxMemberResponseBody as CreatePublicMailboxMemberResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreatePublicMailboxMemberResponse(BaseResponse):
    data: CreatePublicMailboxMemberResponseBody | None
    def __init__(self, d=None) -> None: ...
