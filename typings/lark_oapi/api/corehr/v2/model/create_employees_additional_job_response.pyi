from .create_employees_additional_job_response_body import CreateEmployeesAdditionalJobResponseBody as CreateEmployeesAdditionalJobResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateEmployeesAdditionalJobResponse(BaseResponse):
    data: CreateEmployeesAdditionalJobResponseBody | None
    def __init__(self, d=None) -> None: ...
