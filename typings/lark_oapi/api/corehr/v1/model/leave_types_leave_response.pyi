from .leave_types_leave_response_body import LeaveTypesLeaveResponseBody as LeaveTypesLeaveResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class LeaveTypesLeaveResponse(BaseResponse):
    data: LeaveTypesLeaveResponseBody | None
    def __init__(self, d=None) -> None: ...
