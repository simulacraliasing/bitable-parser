from .instance_view_calendar_event_response_body import InstanceViewCalendarEventResponseBody as InstanceViewCalendarEventResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class InstanceViewCalendarEventResponse(BaseResponse):
    data: InstanceViewCalendarEventResponseBody | None
    def __init__(self, d=None) -> None: ...
