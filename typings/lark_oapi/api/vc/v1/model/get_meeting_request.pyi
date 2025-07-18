from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class GetMeetingRequest(BaseRequest):
    with_participants: bool | None
    with_meeting_ability: bool | None
    user_id_type: str | None
    meeting_id: int | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> GetMeetingRequestBuilder: ...

class GetMeetingRequestBuilder:
    def __init__(self) -> None: ...
    def with_participants(self, with_participants: bool) -> GetMeetingRequestBuilder: ...
    def with_meeting_ability(self, with_meeting_ability: bool) -> GetMeetingRequestBuilder: ...
    def user_id_type(self, user_id_type: str) -> GetMeetingRequestBuilder: ...
    def meeting_id(self, meeting_id: int) -> GetMeetingRequestBuilder: ...
    def build(self) -> GetMeetingRequest: ...
