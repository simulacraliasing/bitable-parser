from .create_working_hours_type_response_body import CreateWorkingHoursTypeResponseBody as CreateWorkingHoursTypeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateWorkingHoursTypeResponse(BaseResponse):
    data: CreateWorkingHoursTypeResponseBody | None
    def __init__(self, d=None) -> None: ...
