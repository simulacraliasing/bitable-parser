from lark_oapi.core.construct import init as init

class LeaveRequestCreatedErrorMessage:
    employment_id: str | None
    leave_type_id: str | None
    start_time: str | None
    end_time: str | None
    code: int | None
    msg: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> LeaveRequestCreatedErrorMessageBuilder: ...

class LeaveRequestCreatedErrorMessageBuilder:
    def __init__(self) -> None: ...
    def employment_id(self, employment_id: str) -> LeaveRequestCreatedErrorMessageBuilder: ...
    def leave_type_id(self, leave_type_id: str) -> LeaveRequestCreatedErrorMessageBuilder: ...
    def start_time(self, start_time: str) -> LeaveRequestCreatedErrorMessageBuilder: ...
    def end_time(self, end_time: str) -> LeaveRequestCreatedErrorMessageBuilder: ...
    def code(self, code: int) -> LeaveRequestCreatedErrorMessageBuilder: ...
    def msg(self, msg: str) -> LeaveRequestCreatedErrorMessageBuilder: ...
    def build(self) -> LeaveRequestCreatedErrorMessage: ...
