from .get_department_response_body import GetDepartmentResponseBody as GetDepartmentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetDepartmentResponse(BaseResponse):
    data: GetDepartmentResponseBody | None
    def __init__(self, d=None) -> None: ...
