from ..model.delete_agent_schedules_request import DeleteAgentSchedulesRequest as DeleteAgentSchedulesRequest
from ..model.delete_agent_schedules_response import DeleteAgentSchedulesResponse as DeleteAgentSchedulesResponse
from ..model.get_agent_schedules_request import GetAgentSchedulesRequest as GetAgentSchedulesRequest
from ..model.get_agent_schedules_response import GetAgentSchedulesResponse as GetAgentSchedulesResponse
from ..model.patch_agent_schedules_request import PatchAgentSchedulesRequest as PatchAgentSchedulesRequest
from ..model.patch_agent_schedules_response import PatchAgentSchedulesResponse as PatchAgentSchedulesResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class AgentSchedules:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def delete(self, request: DeleteAgentSchedulesRequest, option: RequestOption | None = None) -> DeleteAgentSchedulesResponse: ...
    async def adelete(self, request: DeleteAgentSchedulesRequest, option: RequestOption | None = None) -> DeleteAgentSchedulesResponse: ...
    def get(self, request: GetAgentSchedulesRequest, option: RequestOption | None = None) -> GetAgentSchedulesResponse: ...
    async def aget(self, request: GetAgentSchedulesRequest, option: RequestOption | None = None) -> GetAgentSchedulesResponse: ...
    def patch(self, request: PatchAgentSchedulesRequest, option: RequestOption | None = None) -> PatchAgentSchedulesResponse: ...
    async def apatch(self, request: PatchAgentSchedulesRequest, option: RequestOption | None = None) -> PatchAgentSchedulesResponse: ...
