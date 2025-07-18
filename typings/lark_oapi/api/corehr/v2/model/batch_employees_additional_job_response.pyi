from .batch_employees_additional_job_response_body import BatchEmployeesAdditionalJobResponseBody as BatchEmployeesAdditionalJobResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchEmployeesAdditionalJobResponse(BaseResponse):
    data: BatchEmployeesAdditionalJobResponseBody | None
    def __init__(self, d=None) -> None: ...
