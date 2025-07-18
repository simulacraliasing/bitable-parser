from .children_department_response_body import ChildrenDepartmentResponseBody as ChildrenDepartmentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ChildrenDepartmentResponse(BaseResponse):
    data: ChildrenDepartmentResponseBody | None
    def __init__(self, d=None) -> None: ...
