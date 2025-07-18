from lark_oapi.core.construct import init as init

class Formula:
    formula: str | None
    formula_value: str | None
    affected_range: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> FormulaBuilder: ...

class FormulaBuilder:
    def __init__(self) -> None: ...
    def formula(self, formula: str) -> FormulaBuilder: ...
    def formula_value(self, formula_value: str) -> FormulaBuilder: ...
    def affected_range(self, affected_range: str) -> FormulaBuilder: ...
    def build(self) -> Formula: ...
