from lark_oapi.core.construct import init as init

class TaskStatus:
    failure_reason: str | None
    status_code: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> TaskStatusBuilder: ...

class TaskStatusBuilder:
    def __init__(self) -> None: ...
    def failure_reason(self, failure_reason: str) -> TaskStatusBuilder: ...
    def status_code(self, status_code: int) -> TaskStatusBuilder: ...
    def build(self) -> TaskStatus: ...
