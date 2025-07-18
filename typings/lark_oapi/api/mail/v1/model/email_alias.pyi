from lark_oapi.core.construct import init as init

class EmailAlias:
    primary_email: str | None
    email_alias: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> EmailAliasBuilder: ...

class EmailAliasBuilder:
    def __init__(self) -> None: ...
    def primary_email(self, primary_email: str) -> EmailAliasBuilder: ...
    def email_alias(self, email_alias: str) -> EmailAliasBuilder: ...
    def build(self) -> EmailAlias: ...
