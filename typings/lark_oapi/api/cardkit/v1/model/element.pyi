from lark_oapi.core.construct import init as init

class Element:
    tag: str | None
    element_id: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ElementBuilder: ...

class ElementBuilder:
    def __init__(self) -> None: ...
    def tag(self, tag: str) -> ElementBuilder: ...
    def element_id(self, element_id: str) -> ElementBuilder: ...
    def build(self) -> Element: ...
