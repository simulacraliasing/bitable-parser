from .get_employee_type_response_body import GetEmployeeTypeResponseBody as GetEmployeeTypeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetEmployeeTypeResponse(BaseResponse):
    data: GetEmployeeTypeResponseBody | None
    def __init__(self, d=None) -> None: ...
