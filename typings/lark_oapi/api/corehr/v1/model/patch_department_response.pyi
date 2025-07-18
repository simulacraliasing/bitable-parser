from .patch_department_response_body import PatchDepartmentResponseBody as PatchDepartmentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchDepartmentResponse(BaseResponse):
    data: PatchDepartmentResponseBody | None
    def __init__(self, d=None) -> None: ...
