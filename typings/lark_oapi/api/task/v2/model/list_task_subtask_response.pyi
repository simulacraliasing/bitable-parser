from .list_task_subtask_response_body import ListTaskSubtaskResponseBody as ListTaskSubtaskResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListTaskSubtaskResponse(BaseResponse):
    data: ListTaskSubtaskResponseBody | None
    def __init__(self, d=None) -> None: ...
