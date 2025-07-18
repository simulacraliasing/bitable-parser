from .list_calendar_event_attendee_response_body import ListCalendarEventAttendeeResponseBody as ListCalendarEventAttendeeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListCalendarEventAttendeeResponse(BaseResponse):
    data: ListCalendarEventAttendeeResponseBody | None
    def __init__(self, d=None) -> None: ...
