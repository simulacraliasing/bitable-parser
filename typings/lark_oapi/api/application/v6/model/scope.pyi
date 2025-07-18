from lark_oapi.core.construct import init as init

class Scope:
    scope_name: str | None
    grant_status: int | None
    scope_type: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ScopeBuilder: ...

class ScopeBuilder:
    def __init__(self) -> None: ...
    def scope_name(self, scope_name: str) -> ScopeBuilder: ...
    def grant_status(self, grant_status: int) -> ScopeBuilder: ...
    def scope_type(self, scope_type: str) -> ScopeBuilder: ...
    def build(self) -> Scope: ...
