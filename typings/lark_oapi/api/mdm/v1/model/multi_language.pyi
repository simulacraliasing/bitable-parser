from lark_oapi.core.construct import init as init

class MultiLanguage:
    language: str | None
    value: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> MultiLanguageBuilder: ...

class MultiLanguageBuilder:
    def __init__(self) -> None: ...
    def language(self, language: str) -> MultiLanguageBuilder: ...
    def value(self, value: str) -> MultiLanguageBuilder: ...
    def build(self) -> MultiLanguage: ...
