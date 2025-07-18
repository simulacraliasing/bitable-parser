from .kickout_meeting_request_body import KickoutMeetingRequestBody as KickoutMeetingRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class KickoutMeetingRequest(BaseRequest):
    user_id_type: str | None
    meeting_id: int | None
    request_body: KickoutMeetingRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> KickoutMeetingRequestBuilder: ...

class KickoutMeetingRequestBuilder:
    def __init__(self) -> None: ...
    def user_id_type(self, user_id_type: str) -> KickoutMeetingRequestBuilder: ...
    def meeting_id(self, meeting_id: int) -> KickoutMeetingRequestBuilder: ...
    def request_body(self, request_body: KickoutMeetingRequestBody) -> KickoutMeetingRequestBuilder: ...
    def build(self) -> KickoutMeetingRequest: ...
