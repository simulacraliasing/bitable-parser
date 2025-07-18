from .create_employees_international_assignment_response_body import CreateEmployeesInternationalAssignmentResponseBody as CreateEmployeesInternationalAssignmentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateEmployeesInternationalAssignmentResponse(BaseResponse):
    data: CreateEmployeesInternationalAssignmentResponseBody | None
    def __init__(self, d=None) -> None: ...
