from .list_department_unit_response_body import ListDepartmentUnitResponseBody as ListDepartmentUnitResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListDepartmentUnitResponse(BaseResponse):
    data: ListDepartmentUnitResponseBody | None
    def __init__(self, d=None) -> None: ...
