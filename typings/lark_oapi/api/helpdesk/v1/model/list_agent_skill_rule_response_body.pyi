from .agent_skill_rule import AgentSkillRule as AgentSkillRule
from lark_oapi.core.construct import init as init

class ListAgentSkillRuleResponseBody:
    rules: list[AgentSkillRule] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ListAgentSkillRuleResponseBodyBuilder: ...

class ListAgentSkillRuleResponseBodyBuilder:
    def __init__(self) -> None: ...
    def rules(self, rules: list[AgentSkillRule]) -> ListAgentSkillRuleResponseBodyBuilder: ...
    def build(self) -> ListAgentSkillRuleResponseBody: ...
