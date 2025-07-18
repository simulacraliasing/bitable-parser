from .user import User as User
from lark_oapi.core.construct import init as init

class QueryUserResponseBody:
    user_list: list[User] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> QueryUserResponseBodyBuilder: ...

class QueryUserResponseBodyBuilder:
    def __init__(self) -> None: ...
    def user_list(self, user_list: list[User]) -> QueryUserResponseBodyBuilder: ...
    def build(self) -> QueryUserResponseBody: ...
