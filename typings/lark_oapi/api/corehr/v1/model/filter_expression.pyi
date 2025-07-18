from .filter_condition import FilterCondition as FilterCondition
from lark_oapi.core.construct import init as init

class FilterExpression:
    conditions: list[FilterCondition] | None
    expression: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> FilterExpressionBuilder: ...

class FilterExpressionBuilder:
    def __init__(self) -> None: ...
    def conditions(self, conditions: list[FilterCondition]) -> FilterExpressionBuilder: ...
    def expression(self, expression: str) -> FilterExpressionBuilder: ...
    def build(self) -> FilterExpression: ...
