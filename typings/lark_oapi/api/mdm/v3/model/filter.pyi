from .expression import Expression as Expression
from lark_oapi.core.construct import init as init

class Filter:
    logic: str | None
    expressions: list[Expression] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> FilterBuilder: ...

class FilterBuilder:
    def __init__(self) -> None: ...
    def logic(self, logic: str) -> FilterBuilder: ...
    def expressions(self, expressions: list[Expression]) -> FilterBuilder: ...
    def build(self) -> Filter: ...
