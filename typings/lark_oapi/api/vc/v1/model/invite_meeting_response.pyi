from .invite_meeting_response_body import InviteMeetingResponseBody as InviteMeetingResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class InviteMeetingResponse(BaseResponse):
    data: InviteMeetingResponseBody | None
    def __init__(self, d=None) -> None: ...
