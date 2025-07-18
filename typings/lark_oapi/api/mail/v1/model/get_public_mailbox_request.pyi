from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class GetPublicMailboxRequest(BaseRequest):
    public_mailbox_id: str | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> GetPublicMailboxRequestBuilder: ...

class GetPublicMailboxRequestBuilder:
    def __init__(self) -> None: ...
    def public_mailbox_id(self, public_mailbox_id: str) -> GetPublicMailboxRequestBuilder: ...
    def build(self) -> GetPublicMailboxRequest: ...
