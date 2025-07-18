from .create_employee_type_response_body import CreateEmployeeTypeResponseBody as CreateEmployeeTypeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateEmployeeTypeResponse(BaseResponse):
    data: CreateEmployeeTypeResponseBody | None
    def __init__(self, d=None) -> None: ...
