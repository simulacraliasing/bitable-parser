from .search_employee_response_body import SearchEmployeeResponseBody as SearchEmployeeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchEmployeeResponse(BaseResponse):
    data: SearchEmployeeResponseBody | None
    def __init__(self, d=None) -> None: ...
