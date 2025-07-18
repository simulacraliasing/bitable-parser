from .patch_employees_international_assignment_response_body import PatchEmployeesInternationalAssignmentResponseBody as PatchEmployeesInternationalAssignmentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchEmployeesInternationalAssignmentResponse(BaseResponse):
    data: PatchEmployeesInternationalAssignmentResponseBody | None
    def __init__(self, d=None) -> None: ...
