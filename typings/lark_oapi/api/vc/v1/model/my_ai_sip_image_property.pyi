from lark_oapi.core.construct import init as init

class MyAiSipImageProperty:
    theme: str | None
    number: int | None
    size: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> MyAiSipImagePropertyBuilder: ...

class MyAiSipImagePropertyBuilder:
    def __init__(self) -> None: ...
    def theme(self, theme: str) -> MyAiSipImagePropertyBuilder: ...
    def number(self, number: int) -> MyAiSipImagePropertyBuilder: ...
    def size(self, size: str) -> MyAiSipImagePropertyBuilder: ...
    def build(self) -> MyAiSipImageProperty: ...
