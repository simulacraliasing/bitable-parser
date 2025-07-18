from .list_external_task_response_body import ListExternalTaskResponseBody as ListExternalTaskResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListExternalTaskResponse(BaseResponse):
    data: ListExternalTaskResponseBody | None
    def __init__(self, d=None) -> None: ...
