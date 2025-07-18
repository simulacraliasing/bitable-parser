from .task import Task as Task
from lark_oapi.core.construct import init as init

class RemoveTasklistTaskResponseBody:
    task: Task | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> RemoveTasklistTaskResponseBodyBuilder: ...

class RemoveTasklistTaskResponseBodyBuilder:
    def __init__(self) -> None: ...
    def task(self, task: Task) -> RemoveTasklistTaskResponseBodyBuilder: ...
    def build(self) -> RemoveTasklistTaskResponseBody: ...
