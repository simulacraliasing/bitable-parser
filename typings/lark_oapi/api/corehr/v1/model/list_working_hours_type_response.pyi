from .list_working_hours_type_response_body import ListWorkingHoursTypeResponseBody as ListWorkingHoursTypeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListWorkingHoursTypeResponse(BaseResponse):
    data: ListWorkingHoursTypeResponseBody | None
    def __init__(self, d=None) -> None: ...
