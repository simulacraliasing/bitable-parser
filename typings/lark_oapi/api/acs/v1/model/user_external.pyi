from lark_oapi.core.construct import init as init

class UserExternal:
    user_type: int | None
    user_id: int | None
    user_name: str | None
    phone_num: str | None
    department_id: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> UserExternalBuilder: ...

class UserExternalBuilder:
    def __init__(self) -> None: ...
    def user_type(self, user_type: int) -> UserExternalBuilder: ...
    def user_id(self, user_id: int) -> UserExternalBuilder: ...
    def user_name(self, user_name: str) -> UserExternalBuilder: ...
    def phone_num(self, phone_num: str) -> UserExternalBuilder: ...
    def department_id(self, department_id: int) -> UserExternalBuilder: ...
    def build(self) -> UserExternal: ...
