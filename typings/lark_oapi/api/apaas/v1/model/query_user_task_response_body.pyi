from .user_task import UserTask as UserTask
from lark_oapi.core.construct import init as init

class QueryUserTaskResponseBody:
    count: str | None
    tasks: list[UserTask] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> QueryUserTaskResponseBodyBuilder: ...

class QueryUserTaskResponseBodyBuilder:
    def __init__(self) -> None: ...
    def count(self, count: str) -> QueryUserTaskResponseBodyBuilder: ...
    def tasks(self, tasks: list[UserTask]) -> QueryUserTaskResponseBodyBuilder: ...
    def build(self) -> QueryUserTaskResponseBody: ...
