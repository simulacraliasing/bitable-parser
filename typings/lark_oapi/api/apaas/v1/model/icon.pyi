from lark_oapi.core.construct import init as init

class Icon:
    source: str | None
    color: str | None
    color_id: str | None
    icon: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> IconBuilder: ...

class IconBuilder:
    def __init__(self) -> None: ...
    def source(self, source: str) -> IconBuilder: ...
    def color(self, color: str) -> IconBuilder: ...
    def color_id(self, color_id: str) -> IconBuilder: ...
    def icon(self, icon: str) -> IconBuilder: ...
    def build(self) -> Icon: ...
