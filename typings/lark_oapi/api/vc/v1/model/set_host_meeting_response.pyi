from .set_host_meeting_response_body import SetHostMeetingResponseBody as SetHostMeetingResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SetHostMeetingResponse(BaseResponse):
    data: SetHostMeetingResponseBody | None
    def __init__(self, d=None) -> None: ...
