from ..model.create_calendar_event_meeting_minute_request import CreateCalendarEventMeetingMinuteRequest as CreateCalendarEventMeetingMinuteRequest
from ..model.create_calendar_event_meeting_minute_response import CreateCalendarEventMeetingMinuteResponse as CreateCalendarEventMeetingMinuteResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class CalendarEventMeetingMinute:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateCalendarEventMeetingMinuteRequest, option: RequestOption | None = None) -> CreateCalendarEventMeetingMinuteResponse: ...
    async def acreate(self, request: CreateCalendarEventMeetingMinuteRequest, option: RequestOption | None = None) -> CreateCalendarEventMeetingMinuteResponse: ...
