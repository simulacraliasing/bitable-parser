from .batch_get_employees_job_data_response_body import BatchGetEmployeesJobDataResponseBody as BatchGetEmployeesJobDataResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchGetEmployeesJobDataResponse(BaseResponse):
    data: BatchGetEmployeesJobDataResponseBody | None
    def __init__(self, d=None) -> None: ...
