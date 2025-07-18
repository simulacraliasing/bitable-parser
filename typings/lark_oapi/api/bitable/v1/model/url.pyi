from lark_oapi.core.construct import init as init

class Url:
    text: str | None
    link: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> UrlBuilder: ...

class UrlBuilder:
    def __init__(self) -> None: ...
    def text(self, text: str) -> UrlBuilder: ...
    def link(self, link: str) -> UrlBuilder: ...
    def build(self) -> Url: ...
