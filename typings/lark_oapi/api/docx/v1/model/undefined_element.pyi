from lark_oapi.core.construct import init as init

class UndefinedElement:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> UndefinedElementBuilder: ...

class UndefinedElementBuilder:
    def __init__(self) -> None: ...
    def build(self) -> UndefinedElement: ...
