from .create_public_mailbox_alias_response_body import CreatePublicMailboxAliasResponseBody as CreatePublicMailboxAliasResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreatePublicMailboxAliasResponse(BaseResponse):
    data: CreatePublicMailboxAliasResponseBody | None
    def __init__(self, d=None) -> None: ...
