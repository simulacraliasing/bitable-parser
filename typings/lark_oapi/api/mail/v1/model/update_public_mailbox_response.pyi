from .update_public_mailbox_response_body import UpdatePublicMailboxResponseBody as UpdatePublicMailboxResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdatePublicMailboxResponse(BaseResponse):
    data: UpdatePublicMailboxResponseBody | None
    def __init__(self, d=None) -> None: ...
