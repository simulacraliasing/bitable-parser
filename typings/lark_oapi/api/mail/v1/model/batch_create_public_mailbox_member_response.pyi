from .batch_create_public_mailbox_member_response_body import BatchCreatePublicMailboxMemberResponseBody as BatchCreatePublicMailboxMemberResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchCreatePublicMailboxMemberResponse(BaseResponse):
    data: BatchCreatePublicMailboxMemberResponseBody | None
    def __init__(self, d=None) -> None: ...
