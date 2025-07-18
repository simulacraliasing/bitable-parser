from .get_meeting_list_response_body import GetMeetingListResponseBody as GetMeetingListResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetMeetingListResponse(BaseResponse):
    data: GetMeetingListResponseBody | None
    def __init__(self, d=None) -> None: ...
