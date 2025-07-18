from .get_public_mailbox_response_body import GetPublicMailboxResponseBody as GetPublicMailboxResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetPublicMailboxResponse(BaseResponse):
    data: GetPublicMailboxResponseBody | None
    def __init__(self, d=None) -> None: ...
