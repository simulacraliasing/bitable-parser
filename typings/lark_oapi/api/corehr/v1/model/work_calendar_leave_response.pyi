from .work_calendar_leave_response_body import WorkCalendarLeaveResponseBody as WorkCalendarLeaveResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class WorkCalendarLeaveResponse(BaseResponse):
    data: WorkCalendarLeaveResponseBody | None
    def __init__(self, d=None) -> None: ...
