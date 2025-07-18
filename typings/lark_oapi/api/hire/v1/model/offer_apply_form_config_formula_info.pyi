from .offer_apply_form_formula_extra_map_info import OfferApplyFormFormulaExtraMapInfo as OfferApplyFormFormulaExtraMapInfo
from lark_oapi.core.construct import init as init

class OfferApplyFormConfigFormulaInfo:
    value: str | None
    result: int | None
    extra_map: list[OfferApplyFormFormulaExtraMapInfo] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> OfferApplyFormConfigFormulaInfoBuilder: ...

class OfferApplyFormConfigFormulaInfoBuilder:
    def __init__(self) -> None: ...
    def value(self, value: str) -> OfferApplyFormConfigFormulaInfoBuilder: ...
    def result(self, result: int) -> OfferApplyFormConfigFormulaInfoBuilder: ...
    def extra_map(self, extra_map: list[OfferApplyFormFormulaExtraMapInfo]) -> OfferApplyFormConfigFormulaInfoBuilder: ...
    def build(self) -> OfferApplyFormConfigFormulaInfo: ...
