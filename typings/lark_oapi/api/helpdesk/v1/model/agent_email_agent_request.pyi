from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class AgentEmailAgentRequest(BaseRequest):
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> AgentEmailAgentRequestBuilder: ...

class AgentEmailAgentRequestBuilder:
    def __init__(self) -> None: ...
    def build(self) -> AgentEmailAgentRequest: ...
