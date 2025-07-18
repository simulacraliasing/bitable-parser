from lark_oapi.core.construct import init as init

class DynamicGroupExpression:
    field: str | None
    operator: str | None
    value: str | None
    values: list[str] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DynamicGroupExpressionBuilder: ...

class DynamicGroupExpressionBuilder:
    def __init__(self) -> None: ...
    def field(self, field: str) -> DynamicGroupExpressionBuilder: ...
    def operator(self, operator: str) -> DynamicGroupExpressionBuilder: ...
    def value(self, value: str) -> DynamicGroupExpressionBuilder: ...
    def values(self, values: list[str]) -> DynamicGroupExpressionBuilder: ...
    def build(self) -> DynamicGroupExpression: ...
