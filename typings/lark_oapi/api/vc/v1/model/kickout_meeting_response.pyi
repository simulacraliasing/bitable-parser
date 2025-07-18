from .kickout_meeting_response_body import KickoutMeetingResponseBody as KickoutMeetingResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class KickoutMeetingResponse(BaseResponse):
    data: KickoutMeetingResponseBody | None
    def __init__(self, d=None) -> None: ...
