from lark_oapi.core.construct import init as init

class MeetingUser:
    id: str | None
    user_type: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> MeetingUserBuilder: ...

class MeetingUserBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> MeetingUserBuilder: ...
    def user_type(self, user_type: int) -> MeetingUserBuilder: ...
    def build(self) -> MeetingUser: ...
