from .create_task_subtask_response_body import CreateTaskSubtaskResponseBody as CreateTaskSubtaskResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateTaskSubtaskResponse(BaseResponse):
    data: CreateTaskSubtaskResponseBody | None
    def __init__(self, d=None) -> None: ...
