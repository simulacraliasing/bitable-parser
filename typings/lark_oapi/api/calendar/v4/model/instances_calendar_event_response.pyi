from .instances_calendar_event_response_body import InstancesCalendarEventResponseBody as InstancesCalendarEventResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class InstancesCalendarEventResponse(BaseResponse):
    data: InstancesCalendarEventResponseBody | None
    def __init__(self, d=None) -> None: ...
