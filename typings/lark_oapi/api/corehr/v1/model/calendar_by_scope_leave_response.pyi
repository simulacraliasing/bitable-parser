from .calendar_by_scope_leave_response_body import CalendarByScopeLeaveResponseBody as CalendarByScopeLeaveResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CalendarByScopeLeaveResponse(BaseResponse):
    data: CalendarByScopeLeaveResponseBody | None
    def __init__(self, d=None) -> None: ...
