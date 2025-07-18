from .search_task_response_body import SearchTaskResponseBody as SearchTaskResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchTaskResponse(BaseResponse):
    data: SearchTaskResponseBody | None
    def __init__(self, d=None) -> None: ...
