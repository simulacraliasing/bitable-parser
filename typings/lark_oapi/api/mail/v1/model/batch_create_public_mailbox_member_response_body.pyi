from .public_mailbox_member import PublicMailboxMember as PublicMailboxMember
from lark_oapi.core.construct import init as init

class BatchCreatePublicMailboxMemberResponseBody:
    items: list[PublicMailboxMember] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> BatchCreatePublicMailboxMemberResponseBodyBuilder: ...

class BatchCreatePublicMailboxMemberResponseBodyBuilder:
    def __init__(self) -> None: ...
    def items(self, items: list[PublicMailboxMember]) -> BatchCreatePublicMailboxMemberResponseBodyBuilder: ...
    def build(self) -> BatchCreatePublicMailboxMemberResponseBody: ...
