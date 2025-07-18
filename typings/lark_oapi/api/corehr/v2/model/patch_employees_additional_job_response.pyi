from .patch_employees_additional_job_response_body import PatchEmployeesAdditionalJobResponseBody as PatchEmployeesAdditionalJobResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchEmployeesAdditionalJobResponse(BaseResponse):
    data: PatchEmployeesAdditionalJobResponseBody | None
    def __init__(self, d=None) -> None: ...
