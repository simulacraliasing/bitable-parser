from .list_department_response_body import ListDepartmentResponseBody as ListDepartmentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListDepartmentResponse(BaseResponse):
    data: ListDepartmentResponseBody | None
    def __init__(self, d=None) -> None: ...
