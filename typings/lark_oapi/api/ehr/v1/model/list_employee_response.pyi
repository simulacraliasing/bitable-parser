from .list_employee_response_body import ListEmployeeResponseBody as ListEmployeeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListEmployeeResponse(BaseResponse):
    data: ListEmployeeResponseBody | None
    def __init__(self, d=None) -> None: ...
