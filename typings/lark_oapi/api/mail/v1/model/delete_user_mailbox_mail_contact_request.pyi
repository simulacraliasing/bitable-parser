from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class DeleteUserMailboxMailContactRequest(BaseRequest):
    user_mailbox_id: str | None
    mail_contact_id: str | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> DeleteUserMailboxMailContactRequestBuilder: ...

class DeleteUserMailboxMailContactRequestBuilder:
    def __init__(self) -> None: ...
    def user_mailbox_id(self, user_mailbox_id: str) -> DeleteUserMailboxMailContactRequestBuilder: ...
    def mail_contact_id(self, mail_contact_id: str) -> DeleteUserMailboxMailContactRequestBuilder: ...
    def build(self) -> DeleteUserMailboxMailContactRequest: ...
