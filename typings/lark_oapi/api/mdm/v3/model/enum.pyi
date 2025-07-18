from lark_oapi.core.construct import init as init

class Enum:
    value: str | None
    multilingual_name: dict[str, str] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> EnumBuilder: ...

class EnumBuilder:
    def __init__(self) -> None: ...
    def value(self, value: str) -> EnumBuilder: ...
    def multilingual_name(self, multilingual_name: dict[str, str]) -> EnumBuilder: ...
    def build(self) -> Enum: ...
