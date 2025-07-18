from .update_department_response_body import UpdateDepartmentResponseBody as UpdateDepartmentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdateDepartmentResponse(BaseResponse):
    data: UpdateDepartmentResponseBody | None
    def __init__(self, d=None) -> None: ...
