from .list_employees_international_assignment_response_body import ListEmployeesInternationalAssignmentResponseBody as ListEmployeesInternationalAssignmentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListEmployeesInternationalAssignmentResponse(BaseResponse):
    data: ListEmployeesInternationalAssignmentResponseBody | None
    def __init__(self, d=None) -> None: ...
