from .update_employee_type_enum_response_body import UpdateEmployeeTypeEnumResponseBody as UpdateEmployeeTypeEnumResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdateEmployeeTypeEnumResponse(BaseResponse):
    data: UpdateEmployeeTypeEnumResponseBody | None
    def __init__(self, d=None) -> None: ...
