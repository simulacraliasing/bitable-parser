from .query_user_task_remedy_response_body import QueryUserTaskRemedyResponseBody as QueryUserTaskRemedyResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryUserTaskRemedyResponse(BaseResponse):
    data: QueryUserTaskRemedyResponseBody | None
    def __init__(self, d=None) -> None: ...
