from .patch_employee_response_body import PatchEmployeeResponseBody as PatchEmployeeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchEmployeeResponse(BaseResponse):
    data: PatchEmployeeResponseBody | None
    def __init__(self, d=None) -> None: ...
