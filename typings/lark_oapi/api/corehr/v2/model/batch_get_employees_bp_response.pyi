from .batch_get_employees_bp_response_body import BatchGetEmployeesBpResponseBody as BatchGetEmployeesBpResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchGetEmployeesBpResponse(BaseResponse):
    data: BatchGetEmployeesBpResponseBody | None
    def __init__(self, d=None) -> None: ...
