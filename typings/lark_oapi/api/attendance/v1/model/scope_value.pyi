from lark_oapi.core.construct import init as init

class ScopeValue:
    key: str | None
    name: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ScopeValueBuilder: ...

class ScopeValueBuilder:
    def __init__(self) -> None: ...
    def key(self, key: str) -> ScopeValueBuilder: ...
    def name(self, name: str) -> ScopeValueBuilder: ...
    def build(self) -> ScopeValue: ...
