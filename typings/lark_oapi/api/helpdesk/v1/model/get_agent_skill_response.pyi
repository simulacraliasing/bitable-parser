from .get_agent_skill_response_body import GetAgentSkillResponseBody as GetAgentSkillResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetAgentSkillResponse(BaseResponse):
    data: GetAgentSkillResponseBody | None
    def __init__(self, d=None) -> None: ...
