from .allowed_rollbaclk_task_item_type import AllowedRollbaclkTaskItemType as AllowedRollbaclkTaskItemType
from lark_oapi.core.construct import init as init

class RollbackPointsUserTaskResponseBody:
    tasks: list[AllowedRollbaclkTaskItemType] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> RollbackPointsUserTaskResponseBodyBuilder: ...

class RollbackPointsUserTaskResponseBodyBuilder:
    def __init__(self) -> None: ...
    def tasks(self, tasks: list[AllowedRollbaclkTaskItemType]) -> RollbackPointsUserTaskResponseBodyBuilder: ...
    def build(self) -> RollbackPointsUserTaskResponseBody: ...
