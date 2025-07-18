from .parent_department_response_body import ParentDepartmentResponseBody as ParentDepartmentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ParentDepartmentResponse(BaseResponse):
    data: ParentDepartmentResponseBody | None
    def __init__(self, d=None) -> None: ...
