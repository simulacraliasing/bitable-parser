from .add_tasklist_task_response_body import AddTasklistTaskResponseBody as AddTasklistTaskResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class AddTasklistTaskResponse(BaseResponse):
    data: AddTasklistTaskResponseBody | None
    def __init__(self, d=None) -> None: ...
