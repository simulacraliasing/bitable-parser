from .leave_request_history_leave_response_body import LeaveRequestHistoryLeaveResponseBody as LeaveRequestHistoryLeaveResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class LeaveRequestHistoryLeaveResponse(BaseResponse):
    data: LeaveRequestHistoryLeaveResponseBody | None
    def __init__(self, d=None) -> None: ...
