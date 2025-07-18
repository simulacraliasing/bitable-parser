from .work_calendar_date_leave_response_body import WorkCalendarDateLeaveResponseBody as WorkCalendarDateLeaveResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class WorkCalendarDateLeaveResponse(BaseResponse):
    data: WorkCalendarDateLeaveResponseBody | None
    def __init__(self, d=None) -> None: ...
