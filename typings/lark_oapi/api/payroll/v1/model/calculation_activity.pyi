from .i18n_content import I18nContent as I18nContent
from lark_oapi.core.construct import init as init

class CalculationActivity:
    calculation_activity_id: int | None
    calculation_activity_names: list[I18nContent] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CalculationActivityBuilder: ...

class CalculationActivityBuilder:
    def __init__(self) -> None: ...
    def calculation_activity_id(self, calculation_activity_id: int) -> CalculationActivityBuilder: ...
    def calculation_activity_names(self, calculation_activity_names: list[I18nContent]) -> CalculationActivityBuilder: ...
    def build(self) -> CalculationActivity: ...
