from .get_employee_response_body import GetEmployeeResponseBody as GetEmployeeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetEmployeeResponse(BaseResponse):
    data: GetEmployeeResponseBody | None
    def __init__(self, d=None) -> None: ...
