from .i18n import I18n as I18n
from lark_oapi.core.construct import init as init

class StandardDimension:
    api_name: str | None
    label: I18n | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> StandardDimensionBuilder: ...

class StandardDimensionBuilder:
    def __init__(self) -> None: ...
    def api_name(self, api_name: str) -> StandardDimensionBuilder: ...
    def label(self, label: I18n) -> StandardDimensionBuilder: ...
    def build(self) -> StandardDimension: ...
