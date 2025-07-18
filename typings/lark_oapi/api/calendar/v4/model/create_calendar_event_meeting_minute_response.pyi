from .create_calendar_event_meeting_minute_response_body import CreateCalendarEventMeetingMinuteResponseBody as CreateCalendarEventMeetingMinuteResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateCalendarEventMeetingMinuteResponse(BaseResponse):
    data: CreateCalendarEventMeetingMinuteResponseBody | None
    def __init__(self, d=None) -> None: ...
