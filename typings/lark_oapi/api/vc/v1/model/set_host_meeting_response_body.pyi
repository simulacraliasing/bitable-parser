from .meeting_user import MeetingUser as MeetingUser
from lark_oapi.core.construct import init as init

class SetHostMeetingResponseBody:
    host_user: MeetingUser | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SetHostMeetingResponseBodyBuilder: ...

class SetHostMeetingResponseBodyBuilder:
    def __init__(self) -> None: ...
    def host_user(self, host_user: MeetingUser) -> SetHostMeetingResponseBodyBuilder: ...
    def build(self) -> SetHostMeetingResponseBody: ...
