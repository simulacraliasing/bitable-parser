from lark_oapi.core.construct import init as init

class LeaveBalancesLeaveRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> LeaveBalancesLeaveRequestBodyBuilder: ...

class LeaveBalancesLeaveRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> LeaveBalancesLeaveRequestBody: ...
