from .get_by_application_employee_response_body import GetByApplicationEmployeeResponseBody as GetByApplicationEmployeeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetByApplicationEmployeeResponse(BaseResponse):
    data: GetByApplicationEmployeeResponseBody | None
    def __init__(self, d=None) -> None: ...
