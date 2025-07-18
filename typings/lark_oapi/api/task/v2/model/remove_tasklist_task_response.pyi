from .remove_tasklist_task_response_body import RemoveTasklistTaskResponseBody as RemoveTasklistTaskResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class RemoveTasklistTaskResponse(BaseResponse):
    data: RemoveTasklistTaskResponseBody | None
    def __init__(self, d=None) -> None: ...
