from .list_task_response_body import ListTaskResponseBody as ListTaskResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListTaskResponse(BaseResponse):
    data: ListTaskResponseBody | None
    def __init__(self, d=None) -> None: ...
