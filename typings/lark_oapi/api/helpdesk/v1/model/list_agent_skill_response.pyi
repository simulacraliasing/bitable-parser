from .list_agent_skill_response_body import ListAgentSkillResponseBody as ListAgentSkillResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListAgentSkillResponse(BaseResponse):
    data: ListAgentSkillResponseBody | None
    def __init__(self, d=None) -> None: ...
