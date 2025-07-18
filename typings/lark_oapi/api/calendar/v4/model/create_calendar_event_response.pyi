from .create_calendar_event_response_body import CreateCalendarEventResponseBody as CreateCalendarEventResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateCalendarEventResponse(BaseResponse):
    data: CreateCalendarEventResponseBody | None
    def __init__(self, d=None) -> None: ...
