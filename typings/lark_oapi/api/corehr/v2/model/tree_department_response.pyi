from .tree_department_response_body import TreeDepartmentResponseBody as TreeDepartmentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class TreeDepartmentResponse(BaseResponse):
    data: TreeDepartmentResponseBody | None
    def __init__(self, d=None) -> None: ...
