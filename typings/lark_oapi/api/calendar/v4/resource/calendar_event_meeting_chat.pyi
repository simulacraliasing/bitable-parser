from ..model.create_calendar_event_meeting_chat_request import CreateCalendarEventMeetingChatRequest as CreateCalendarEventMeetingChatRequest
from ..model.create_calendar_event_meeting_chat_response import CreateCalendarEventMeetingChatResponse as CreateCalendarEventMeetingChatResponse
from ..model.delete_calendar_event_meeting_chat_request import DeleteCalendarEventMeetingChatRequest as DeleteCalendarEventMeetingChatRequest
from ..model.delete_calendar_event_meeting_chat_response import DeleteCalendarEventMeetingChatResponse as DeleteCalendarEventMeetingChatResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class CalendarEventMeetingChat:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateCalendarEventMeetingChatRequest, option: RequestOption | None = None) -> CreateCalendarEventMeetingChatResponse: ...
    async def acreate(self, request: CreateCalendarEventMeetingChatRequest, option: RequestOption | None = None) -> CreateCalendarEventMeetingChatResponse: ...
    def delete(self, request: DeleteCalendarEventMeetingChatRequest, option: RequestOption | None = None) -> DeleteCalendarEventMeetingChatResponse: ...
    async def adelete(self, request: DeleteCalendarEventMeetingChatRequest, option: RequestOption | None = None) -> DeleteCalendarEventMeetingChatResponse: ...
