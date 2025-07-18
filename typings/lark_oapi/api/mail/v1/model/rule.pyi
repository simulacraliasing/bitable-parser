from .rule_action import RuleAction as RuleAction
from .rule_condition import RuleCondition as RuleCondition
from lark_oapi.core.construct import init as init

class Rule:
    id: int | None
    condition: RuleCondition | None
    action: RuleAction | None
    ignore_the_rest_of_rules: bool | None
    name: str | None
    is_enable: bool | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> RuleBuilder: ...

class RuleBuilder:
    def __init__(self) -> None: ...
    def id(self, id: int) -> RuleBuilder: ...
    def condition(self, condition: RuleCondition) -> RuleBuilder: ...
    def action(self, action: RuleAction) -> RuleBuilder: ...
    def ignore_the_rest_of_rules(self, ignore_the_rest_of_rules: bool) -> RuleBuilder: ...
    def name(self, name: str) -> RuleBuilder: ...
    def is_enable(self, is_enable: bool) -> RuleBuilder: ...
    def build(self) -> Rule: ...
