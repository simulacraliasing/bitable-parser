from .user_task_remedy import UserTaskRemedy as UserTaskRemedy
from lark_oapi.core.construct import init as init

class QueryUserTaskRemedyResponseBody:
    user_remedys: list[UserTaskRemedy] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> QueryUserTaskRemedyResponseBodyBuilder: ...

class QueryUserTaskRemedyResponseBodyBuilder:
    def __init__(self) -> None: ...
    def user_remedys(self, user_remedys: list[UserTaskRemedy]) -> QueryUserTaskRemedyResponseBodyBuilder: ...
    def build(self) -> QueryUserTaskRemedyResponseBody: ...
