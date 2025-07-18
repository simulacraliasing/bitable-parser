from .role_authorization import RoleAuthorization as RoleAuthorization
from lark_oapi.core.construct import init as init

class QueryAuthorizationResponseBody:
    items: list[RoleAuthorization] | None
    has_more: bool | None
    page_token: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> QueryAuthorizationResponseBodyBuilder: ...

class QueryAuthorizationResponseBodyBuilder:
    def __init__(self) -> None: ...
    def items(self, items: list[RoleAuthorization]) -> QueryAuthorizationResponseBodyBuilder: ...
    def has_more(self, has_more: bool) -> QueryAuthorizationResponseBodyBuilder: ...
    def page_token(self, page_token: str) -> QueryAuthorizationResponseBodyBuilder: ...
    def build(self) -> QueryAuthorizationResponseBody: ...
