from .search_calendar_response_body import SearchCalendarResponseBody as SearchCalendarResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchCalendarResponse(BaseResponse):
    data: SearchCalendarResponseBody | None
    def __init__(self, d=None) -> None: ...
