from lark_oapi.core.construct import init as init

class MemoryMessage:
    role: str | None
    content: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> MemoryMessageBuilder: ...

class MemoryMessageBuilder:
    def __init__(self) -> None: ...
    def role(self, role: str) -> MemoryMessageBuilder: ...
    def content(self, content: str) -> MemoryMessageBuilder: ...
    def build(self) -> MemoryMessage: ...
