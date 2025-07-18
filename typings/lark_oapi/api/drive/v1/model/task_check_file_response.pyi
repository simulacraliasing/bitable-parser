from .task_check_file_response_body import TaskCheckFileResponseBody as TaskCheckFileResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class TaskCheckFileResponse(BaseResponse):
    data: TaskCheckFileResponseBody | None
    def __init__(self, d=None) -> None: ...
