from .search_calendar_event_response_body import SearchCalendarEventResponseBody as SearchCalendarEventResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchCalendarEventResponse(BaseResponse):
    data: SearchCalendarEventResponseBody | None
    def __init__(self, d=None) -> None: ...
