from .list_by_no_meeting_response_body import ListByNoMeetingResponseBody as ListByNoMeetingResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListByNoMeetingResponse(BaseResponse):
    data: ListByNoMeetingResponseBody | None
    def __init__(self, d=None) -> None: ...
