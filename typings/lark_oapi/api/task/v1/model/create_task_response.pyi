from .create_task_response_body import CreateTaskResponseBody as CreateTaskResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateTaskResponse(BaseResponse):
    data: CreateTaskResponseBody | None
    def __init__(self, d=None) -> None: ...
