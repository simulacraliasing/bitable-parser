from .get_task_response_body import GetTaskResponseBody as GetTaskResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetTaskResponse(BaseResponse):
    data: GetTaskResponseBody | None
    def __init__(self, d=None) -> None: ...
