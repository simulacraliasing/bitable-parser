from .create_calendar_response_body import CreateCalendarResponseBody as CreateCalendarResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateCalendarResponse(BaseResponse):
    data: CreateCalendarResponseBody | None
    def __init__(self, d=None) -> None: ...
