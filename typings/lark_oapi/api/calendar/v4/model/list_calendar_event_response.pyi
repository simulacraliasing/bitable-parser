from .list_calendar_event_response_body import ListCalendarEventResponseBody as ListCalendarEventResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListCalendarEventResponse(BaseResponse):
    data: ListCalendarEventResponseBody | None
    def __init__(self, d=None) -> None: ...
