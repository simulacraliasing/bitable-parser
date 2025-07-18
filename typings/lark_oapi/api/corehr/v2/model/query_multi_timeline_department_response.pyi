from .query_multi_timeline_department_response_body import QueryMultiTimelineDepartmentResponseBody as QueryMultiTimelineDepartmentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryMultiTimelineDepartmentResponse(BaseResponse):
    data: QueryMultiTimelineDepartmentResponseBody | None
    def __init__(self, d=None) -> None: ...
