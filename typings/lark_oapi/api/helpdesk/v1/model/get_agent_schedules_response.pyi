from .get_agent_schedules_response_body import GetAgentSchedulesResponseBody as GetAgentSchedulesResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetAgentSchedulesResponse(BaseResponse):
    data: GetAgentSchedulesResponseBody | None
    def __init__(self, d=None) -> None: ...
