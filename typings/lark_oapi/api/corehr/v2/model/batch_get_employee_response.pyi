from .batch_get_employee_response_body import BatchGetEmployeeResponseBody as BatchGetEmployeeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchGetEmployeeResponse(BaseResponse):
    data: BatchGetEmployeeResponseBody | None
    def __init__(self, d=None) -> None: ...
