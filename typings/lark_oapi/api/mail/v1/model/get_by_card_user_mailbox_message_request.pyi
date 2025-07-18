from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class GetByCardUserMailboxMessageRequest(BaseRequest):
    card_id: str | None
    owner_id: str | None
    user_id_type: str | None
    user_mailbox_id: str | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> GetByCardUserMailboxMessageRequestBuilder: ...

class GetByCardUserMailboxMessageRequestBuilder:
    def __init__(self) -> None: ...
    def card_id(self, card_id: str) -> GetByCardUserMailboxMessageRequestBuilder: ...
    def owner_id(self, owner_id: str) -> GetByCardUserMailboxMessageRequestBuilder: ...
    def user_id_type(self, user_id_type: str) -> GetByCardUserMailboxMessageRequestBuilder: ...
    def user_mailbox_id(self, user_mailbox_id: str) -> GetByCardUserMailboxMessageRequestBuilder: ...
    def build(self) -> GetByCardUserMailboxMessageRequest: ...
