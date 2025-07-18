from .patch_calendar_event_response_body import PatchCalendarEventResponseBody as PatchCalendarEventResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchCalendarEventResponse(BaseResponse):
    data: PatchCalendarEventResponseBody | None
    def __init__(self, d=None) -> None: ...
