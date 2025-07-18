from .query_timeline_department_response_body import QueryTimelineDepartmentResponseBody as QueryTimelineDepartmentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryTimelineDepartmentResponse(BaseResponse):
    data: QueryTimelineDepartmentResponseBody | None
    def __init__(self, d=None) -> None: ...
