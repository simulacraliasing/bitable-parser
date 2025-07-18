from lark_oapi.core.construct import init as init

class MetaFailed:
    token: str | None
    code: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> MetaFailedBuilder: ...

class MetaFailedBuilder:
    def __init__(self) -> None: ...
    def token(self, token: str) -> MetaFailedBuilder: ...
    def code(self, code: int) -> MetaFailedBuilder: ...
    def build(self) -> MetaFailed: ...
