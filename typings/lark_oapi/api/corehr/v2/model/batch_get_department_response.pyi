from .batch_get_department_response_body import BatchGetDepartmentResponseBody as BatchGetDepartmentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchGetDepartmentResponse(BaseResponse):
    data: BatchGetDepartmentResponseBody | None
    def __init__(self, d=None) -> None: ...
