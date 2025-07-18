from lark_oapi.core.construct import init as init

class CreateCalendarEventMeetingChatResponseBody:
    meeting_chat_id: str | None
    applink: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CreateCalendarEventMeetingChatResponseBodyBuilder: ...

class CreateCalendarEventMeetingChatResponseBodyBuilder:
    def __init__(self) -> None: ...
    def meeting_chat_id(self, meeting_chat_id: str) -> CreateCalendarEventMeetingChatResponseBodyBuilder: ...
    def applink(self, applink: str) -> CreateCalendarEventMeetingChatResponseBodyBuilder: ...
    def build(self) -> CreateCalendarEventMeetingChatResponseBody: ...
