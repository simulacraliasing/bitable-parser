from .agent_skill import AgentSkill as AgentSkill
from lark_oapi.core.construct import init as init

class PatchAgentSkillRequestBody:
    agent_skill: AgentSkill | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> PatchAgentSkillRequestBodyBuilder: ...

class PatchAgentSkillRequestBodyBuilder:
    def __init__(self) -> None: ...
    def agent_skill(self, agent_skill: AgentSkill) -> PatchAgentSkillRequestBodyBuilder: ...
    def build(self) -> PatchAgentSkillRequestBody: ...
