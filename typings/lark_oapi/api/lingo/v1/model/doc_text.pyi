from lark_oapi.core.construct import init as init

class DocText:
    text: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DocTextBuilder: ...

class DocTextBuilder:
    def __init__(self) -> None: ...
    def text(self, text: str) -> DocTextBuilder: ...
    def build(self) -> DocText: ...
