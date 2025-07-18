from .query_user_task_response_body import QueryUserTaskResponseBody as QueryUserTaskResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryUserTaskResponse(BaseResponse):
    data: QueryUserTaskResponseBody | None
    def __init__(self, d=None) -> None: ...
