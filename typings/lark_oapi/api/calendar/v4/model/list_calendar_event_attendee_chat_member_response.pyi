from .list_calendar_event_attendee_chat_member_response_body import ListCalendarEventAttendeeChatMemberResponseBody as ListCalendarEventAttendeeChatMemberResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListCalendarEventAttendeeChatMemberResponse(BaseResponse):
    data: ListCalendarEventAttendeeChatMemberResponseBody | None
    def __init__(self, d=None) -> None: ...
