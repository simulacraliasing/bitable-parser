from .create_public_mailbox_response_body import CreatePublicMailboxResponseBody as CreatePublicMailboxResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreatePublicMailboxResponse(BaseResponse):
    data: CreatePublicMailboxResponseBody | None
    def __init__(self, d=None) -> None: ...
