from .get_calendar_response_body import GetCalendarResponseBody as GetCalendarResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetCalendarResponse(BaseResponse):
    data: GetCalendarResponseBody | None
    def __init__(self, d=None) -> None: ...
