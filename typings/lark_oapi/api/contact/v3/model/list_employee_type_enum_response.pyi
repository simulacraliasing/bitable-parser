from .list_employee_type_enum_response_body import ListEmployeeTypeEnumResponseBody as ListEmployeeTypeEnumResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListEmployeeTypeEnumResponse(BaseResponse):
    data: ListEmployeeTypeEnumResponseBody | None
    def __init__(self, d=None) -> None: ...
