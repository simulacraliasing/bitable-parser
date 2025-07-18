from lark_oapi.core.construct import init as init

class DocxSource:
    token: str | None
    block_id: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DocxSourceBuilder: ...

class DocxSourceBuilder:
    def __init__(self) -> None: ...
    def token(self, token: str) -> DocxSourceBuilder: ...
    def block_id(self, block_id: str) -> DocxSourceBuilder: ...
    def build(self) -> DocxSource: ...
