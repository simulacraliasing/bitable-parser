from .agent_email_agent_response_body import AgentEmailAgentResponseBody as AgentEmailAgentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class AgentEmailAgentResponse(BaseResponse):
    data: AgentEmailAgentResponseBody | None
    def __init__(self, d=None) -> None: ...
