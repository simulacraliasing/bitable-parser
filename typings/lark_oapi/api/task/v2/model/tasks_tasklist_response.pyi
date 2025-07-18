from .tasks_tasklist_response_body import TasksTasklistResponseBody as TasksTasklistResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class TasksTasklistResponse(BaseResponse):
    data: TasksTasklistResponseBody | None
    def __init__(self, d=None) -> None: ...
