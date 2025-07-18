from .tasklists_task_response_body import TasklistsTaskResponseBody as TasklistsTaskResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class TasklistsTaskResponse(BaseResponse):
    data: TasklistsTaskResponseBody | None
    def __init__(self, d=None) -> None: ...
