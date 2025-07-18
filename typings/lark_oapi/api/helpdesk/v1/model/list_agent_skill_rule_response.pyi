from .list_agent_skill_rule_response_body import ListAgentSkillRuleResponseBody as ListAgentSkillRuleResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListAgentSkillRuleResponse(BaseResponse):
    data: ListAgentSkillRuleResponseBody | None
    def __init__(self, d=None) -> None: ...
