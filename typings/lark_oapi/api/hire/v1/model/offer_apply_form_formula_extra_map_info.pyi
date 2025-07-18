from .i18n import I18n as I18n
from lark_oapi.core.construct import init as init

class OfferApplyFormFormulaExtraMapInfo:
    key: str | None
    value: I18n | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> OfferApplyFormFormulaExtraMapInfoBuilder: ...

class OfferApplyFormFormulaExtraMapInfoBuilder:
    def __init__(self) -> None: ...
    def key(self, key: str) -> OfferApplyFormFormulaExtraMapInfoBuilder: ...
    def value(self, value: I18n) -> OfferApplyFormFormulaExtraMapInfoBuilder: ...
    def build(self) -> OfferApplyFormFormulaExtraMapInfo: ...
