from .subscribe_calendar_response_body import SubscribeCalendarResponseBody as SubscribeCalendarResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SubscribeCalendarResponse(BaseResponse):
    data: SubscribeCalendarResponseBody | None
    def __init__(self, d=None) -> None: ...
