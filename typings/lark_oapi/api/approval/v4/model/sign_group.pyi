from .user_id import UserId as UserId
from lark_oapi.core.construct import init as init

class SignGroup:
    instance_code: str | None
    user_id: UserId | None
    account_code: str | None
    boilerplate_unique_code: str | None
    start_time: int | None
    end_time: int | None
    type: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SignGroupBuilder: ...

class SignGroupBuilder:
    def __init__(self) -> None: ...
    def instance_code(self, instance_code: str) -> SignGroupBuilder: ...
    def user_id(self, user_id: UserId) -> SignGroupBuilder: ...
    def account_code(self, account_code: str) -> SignGroupBuilder: ...
    def boilerplate_unique_code(self, boilerplate_unique_code: str) -> SignGroupBuilder: ...
    def start_time(self, start_time: int) -> SignGroupBuilder: ...
    def end_time(self, end_time: int) -> SignGroupBuilder: ...
    def type(self, type: str) -> SignGroupBuilder: ...
    def build(self) -> SignGroup: ...
