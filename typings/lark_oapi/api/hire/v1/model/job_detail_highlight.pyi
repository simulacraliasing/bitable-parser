from .i18n import I18n as I18n
from lark_oapi.core.construct import init as init

class JobDetailHighlight:
    id: str | None
    name: I18n | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> JobDetailHighlightBuilder: ...

class JobDetailHighlightBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> JobDetailHighlightBuilder: ...
    def name(self, name: I18n) -> JobDetailHighlightBuilder: ...
    def build(self) -> JobDetailHighlight: ...
