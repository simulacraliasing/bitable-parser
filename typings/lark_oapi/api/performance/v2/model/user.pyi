from lark_oapi.core.construct import init as init

class User:
    open_id: str | None
    user_id: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> UserBuilder: ...

class UserBuilder:
    def __init__(self) -> None: ...
    def open_id(self, open_id: str) -> UserBuilder: ...
    def user_id(self, user_id: str) -> UserBuilder: ...
    def build(self) -> User: ...
