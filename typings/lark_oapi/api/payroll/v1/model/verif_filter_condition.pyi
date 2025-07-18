from .verif_filter_value import VerifFilterValue as VerifFilterValue
from lark_oapi.core.construct import init as init

class VerifFilterCondition:
    left_value: VerifFilterValue | None
    operator_type: int | None
    right_values: list[VerifFilterValue] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> VerifFilterConditionBuilder: ...

class VerifFilterConditionBuilder:
    def __init__(self) -> None: ...
    def left_value(self, left_value: VerifFilterValue) -> VerifFilterConditionBuilder: ...
    def operator_type(self, operator_type: int) -> VerifFilterConditionBuilder: ...
    def right_values(self, right_values: list[VerifFilterValue]) -> VerifFilterConditionBuilder: ...
    def build(self) -> VerifFilterCondition: ...
