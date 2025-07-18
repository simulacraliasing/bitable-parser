from .list_calendar_response_body import ListCalendarResponseBody as ListCalendarResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListCalendarResponse(BaseResponse):
    data: ListCalendarResponseBody | None
    def __init__(self, d=None) -> None: ...
