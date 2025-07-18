from .condition_value import ConditionValue as ConditionValue
from lark_oapi.core.construct import init as init

class Condition:
    index: str | None
    left: ConditionValue | None
    right: ConditionValue | None
    operator: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ConditionBuilder: ...

class ConditionBuilder:
    def __init__(self) -> None: ...
    def index(self, index: str) -> ConditionBuilder: ...
    def left(self, left: ConditionValue) -> ConditionBuilder: ...
    def right(self, right: ConditionValue) -> ConditionBuilder: ...
    def operator(self, operator: str) -> ConditionBuilder: ...
    def build(self) -> Condition: ...
