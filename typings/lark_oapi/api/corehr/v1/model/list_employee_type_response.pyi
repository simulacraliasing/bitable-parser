from .list_employee_type_response_body import ListEmployeeTypeResponseBody as ListEmployeeTypeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListEmployeeTypeResponse(BaseResponse):
    data: ListEmployeeTypeResponseBody | None
    def __init__(self, d=None) -> None: ...
