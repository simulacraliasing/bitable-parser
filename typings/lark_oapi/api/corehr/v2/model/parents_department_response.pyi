from .parents_department_response_body import ParentsDepartmentResponseBody as ParentsDepartmentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ParentsDepartmentResponse(BaseResponse):
    data: ParentsDepartmentResponseBody | None
    def __init__(self, d=None) -> None: ...
