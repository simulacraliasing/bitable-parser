from .create_agent_skill_response_body import CreateAgentSkillResponseBody as CreateAgentSkillResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateAgentSkillResponse(BaseResponse):
    data: CreateAgentSkillResponseBody | None
    def __init__(self, d=None) -> None: ...
