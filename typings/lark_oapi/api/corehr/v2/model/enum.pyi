from .i18n import I18n as I18n
from lark_oapi.core.construct import init as init

class Enum:
    enum_name: str | None
    display: list[I18n] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> EnumBuilder: ...

class EnumBuilder:
    def __init__(self) -> None: ...
    def enum_name(self, enum_name: str) -> EnumBuilder: ...
    def display(self, display: list[I18n]) -> EnumBuilder: ...
    def build(self) -> Enum: ...
