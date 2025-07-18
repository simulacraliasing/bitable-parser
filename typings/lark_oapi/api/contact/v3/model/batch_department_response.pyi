from .batch_department_response_body import BatchDepartmentResponseBody as BatchDepartmentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchDepartmentResponse(BaseResponse):
    data: BatchDepartmentResponseBody | None
    def __init__(self, d=None) -> None: ...
