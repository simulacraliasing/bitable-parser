from .get_by_department_bp_response_body import GetByDepartmentBpResponseBody as GetByDepartmentBpResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetByDepartmentBpResponse(BaseResponse):
    data: GetByDepartmentBpResponseBody | None
    def __init__(self, d=None) -> None: ...
