from .query_user_allowed_remedys_user_task_remedy_response_body import QueryUserAllowedRemedysUserTaskRemedyResponseBody as QueryUserAllowedRemedysUserTaskRemedyResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryUserAllowedRemedysUserTaskRemedyResponse(BaseResponse):
    data: QueryUserAllowedRemedysUserTaskRemedyResponseBody | None
    def __init__(self, d=None) -> None: ...
