from .get_calendar_event_response_body import GetCalendarEventResponseBody as GetCalendarEventResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetCalendarEventResponse(BaseResponse):
    data: GetCalendarEventResponseBody | None
    def __init__(self, d=None) -> None: ...
