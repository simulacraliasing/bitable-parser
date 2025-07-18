from .leave_balances_leave_response_body import LeaveBalancesLeaveResponseBody as LeaveBalancesLeaveResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class LeaveBalancesLeaveResponse(BaseResponse):
    data: LeaveBalancesLeaveResponseBody | None
    def __init__(self, d=None) -> None: ...
