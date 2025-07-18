from .query_operation_logs_department_response_body import QueryOperationLogsDepartmentResponseBody as QueryOperationLogsDepartmentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryOperationLogsDepartmentResponse(BaseResponse):
    data: QueryOperationLogsDepartmentResponseBody | None
    def __init__(self, d=None) -> None: ...
