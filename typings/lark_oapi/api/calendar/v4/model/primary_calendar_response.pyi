from .primary_calendar_response_body import PrimaryCalendarResponseBody as PrimaryCalendarResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PrimaryCalendarResponse(BaseResponse):
    data: PrimaryCalendarResponseBody | None
    def __init__(self, d=None) -> None: ...
