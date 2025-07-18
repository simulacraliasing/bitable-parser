from lark_oapi.core.construct import init as init

class KrContent:
    zh: str | None
    en: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> KrContentBuilder: ...

class KrContentBuilder:
    def __init__(self) -> None: ...
    def zh(self, zh: str) -> KrContentBuilder: ...
    def en(self, en: str) -> KrContentBuilder: ...
    def build(self) -> KrContent: ...
