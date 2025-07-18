from .get_working_hours_type_response_body import GetWorkingHoursTypeResponseBody as GetWorkingHoursTypeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetWorkingHoursTypeResponse(BaseResponse):
    data: GetWorkingHoursTypeResponseBody | None
    def __init__(self, d=None) -> None: ...
