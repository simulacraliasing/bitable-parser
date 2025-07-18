from .list_agent_schedule_response_body import ListAgentScheduleResponseBody as ListAgentScheduleResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListAgentScheduleResponse(BaseResponse):
    data: ListAgentScheduleResponseBody | None
    def __init__(self, d=None) -> None: ...
