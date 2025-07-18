from .get_meeting_response_body import GetMeetingResponseBody as GetMeetingResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetMeetingResponse(BaseResponse):
    data: GetMeetingResponseBody | None
    def __init__(self, d=None) -> None: ...
