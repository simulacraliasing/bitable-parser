from lark_oapi.core.construct import init as init

class CustomName:
    zh_cn: str | None
    en_us: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CustomNameBuilder: ...

class CustomNameBuilder:
    def __init__(self) -> None: ...
    def zh_cn(self, zh_cn: str) -> CustomNameBuilder: ...
    def en_us(self, en_us: str) -> CustomNameBuilder: ...
    def build(self) -> CustomName: ...
