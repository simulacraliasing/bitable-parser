from .create_employee_response_body import CreateEmployeeResponseBody as CreateEmployeeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateEmployeeResponse(BaseResponse):
    data: CreateEmployeeResponseBody | None
    def __init__(self, d=None) -> None: ...
