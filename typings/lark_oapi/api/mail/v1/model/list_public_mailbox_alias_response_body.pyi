from .email_alias import EmailAlias as EmailAlias
from lark_oapi.core.construct import init as init

class ListPublicMailboxAliasResponseBody:
    items: list[EmailAlias] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ListPublicMailboxAliasResponseBodyBuilder: ...

class ListPublicMailboxAliasResponseBodyBuilder:
    def __init__(self) -> None: ...
    def items(self, items: list[EmailAlias]) -> ListPublicMailboxAliasResponseBodyBuilder: ...
    def build(self) -> ListPublicMailboxAliasResponseBody: ...
