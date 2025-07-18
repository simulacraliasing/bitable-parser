from .get_meeting_recording_response_body import GetMeetingRecordingResponseBody as GetMeetingRecordingResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetMeetingRecordingResponse(BaseResponse):
    data: GetMeetingRecordingResponseBody | None
    def __init__(self, d=None) -> None: ...
