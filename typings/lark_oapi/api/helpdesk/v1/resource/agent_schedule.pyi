from ..model.create_agent_schedule_request import CreateAgentScheduleRequest as CreateAgentScheduleRequest
from ..model.create_agent_schedule_response import CreateAgentScheduleResponse as CreateAgentScheduleResponse
from ..model.list_agent_schedule_request import ListAgentScheduleRequest as ListAgentScheduleRequest
from ..model.list_agent_schedule_response import ListAgentScheduleResponse as ListAgentScheduleResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class AgentSchedule:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateAgentScheduleRequest, option: RequestOption | None = None) -> CreateAgentScheduleResponse: ...
    async def acreate(self, request: CreateAgentScheduleRequest, option: RequestOption | None = None) -> CreateAgentScheduleResponse: ...
    def list(self, request: ListAgentScheduleRequest, option: RequestOption | None = None) -> ListAgentScheduleResponse: ...
    async def alist(self, request: ListAgentScheduleRequest, option: RequestOption | None = None) -> ListAgentScheduleResponse: ...
