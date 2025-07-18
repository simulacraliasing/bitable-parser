from .search_department_response_body import SearchDepartmentResponseBody as SearchDepartmentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchDepartmentResponse(BaseResponse):
    data: SearchDepartmentResponseBody | None
    def __init__(self, d=None) -> None: ...
