from .patch_public_mailbox_response_body import PatchPublicMailboxResponseBody as PatchPublicMailboxResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchPublicMailboxResponse(BaseResponse):
    data: PatchPublicMailboxResponseBody | None
    def __init__(self, d=None) -> None: ...
