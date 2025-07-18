from .user import User as User
from lark_oapi.core.construct import init as init

class CreateUserResponseBody:
    user: User | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CreateUserResponseBodyBuilder: ...

class CreateUserResponseBodyBuilder:
    def __init__(self) -> None: ...
    def user(self, user: User) -> CreateUserResponseBodyBuilder: ...
    def build(self) -> CreateUserResponseBody: ...
