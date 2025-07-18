from .create_calendar_event_attendee_response_body import CreateCalendarEventAttendeeResponseBody as CreateCalendarEventAttendeeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateCalendarEventAttendeeResponse(BaseResponse):
    data: CreateCalendarEventAttendeeResponseBody | None
    def __init__(self, d=None) -> None: ...
