from lark_oapi.core.construct import init as init

class UpdateTaskRequest:
    task_id: str | None
    folded: bool | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> UpdateTaskRequestBuilder: ...

class UpdateTaskRequestBuilder:
    def __init__(self) -> None: ...
    def task_id(self, task_id: str) -> UpdateTaskRequestBuilder: ...
    def folded(self, folded: bool) -> UpdateTaskRequestBuilder: ...
    def build(self) -> UpdateTaskRequest: ...
