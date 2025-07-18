from .create_employee_type_enum_response_body import CreateEmployeeTypeEnumResponseBody as CreateEmployeeTypeEnumResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateEmployeeTypeEnumResponse(BaseResponse):
    data: CreateEmployeeTypeEnumResponseBody | None
    def __init__(self, d=None) -> None: ...
