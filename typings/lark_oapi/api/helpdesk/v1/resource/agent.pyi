from ..model.agent_email_agent_request import AgentEmailAgentRequest as AgentEmailAgentRequest
from ..model.agent_email_agent_response import AgentEmailAgentResponse as AgentEmailAgentResponse
from ..model.patch_agent_request import PatchAgentRequest as PatchAgentRequest
from ..model.patch_agent_response import PatchAgentResponse as PatchAgentResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class Agent:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def agent_email(self, request: AgentEmailAgentRequest, option: RequestOption | None = None) -> AgentEmailAgentResponse: ...
    async def aagent_email(self, request: AgentEmailAgentRequest, option: RequestOption | None = None) -> AgentEmailAgentResponse: ...
    def patch(self, request: PatchAgentRequest, option: RequestOption | None = None) -> PatchAgentResponse: ...
    async def apatch(self, request: PatchAgentRequest, option: RequestOption | None = None) -> PatchAgentResponse: ...
