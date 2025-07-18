from .create_calendar_event_meeting_chat_response_body import CreateCalendarEventMeetingChatResponseBody as CreateCalendarEventMeetingChatResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateCalendarEventMeetingChatResponse(BaseResponse):
    data: CreateCalendarEventMeetingChatResponseBody | None
    def __init__(self, d=None) -> None: ...
