from .create_department_response_body import CreateDepartmentResponseBody as CreateDepartmentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateDepartmentResponse(BaseResponse):
    data: CreateDepartmentResponseBody | None
    def __init__(self, d=None) -> None: ...
