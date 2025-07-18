from .rec_rule_condition import RecRuleCondition as RecRuleCondition
from lark_oapi.core.construct import init as init

class RecRule:
    conditions: list[RecRuleCondition] | None
    conjunction: str | None
    perm: int | None
    other_perm: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> RecRuleBuilder: ...

class RecRuleBuilder:
    def __init__(self) -> None: ...
    def conditions(self, conditions: list[RecRuleCondition]) -> RecRuleBuilder: ...
    def conjunction(self, conjunction: str) -> RecRuleBuilder: ...
    def perm(self, perm: int) -> RecRuleBuilder: ...
    def other_perm(self, other_perm: int) -> RecRuleBuilder: ...
    def build(self) -> RecRule: ...
