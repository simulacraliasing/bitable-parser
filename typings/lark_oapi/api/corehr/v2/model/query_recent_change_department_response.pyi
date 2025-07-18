from .query_recent_change_department_response_body import QueryRecentChangeDepartmentResponseBody as QueryRecentChangeDepartmentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryRecentChangeDepartmentResponse(BaseResponse):
    data: QueryRecentChangeDepartmentResponseBody | None
    def __init__(self, d=None) -> None: ...
