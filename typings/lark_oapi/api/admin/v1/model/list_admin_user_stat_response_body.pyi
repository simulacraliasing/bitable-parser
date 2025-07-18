from .admin_user_stat import AdminUserStat as AdminUserStat
from lark_oapi.core.construct import init as init

class ListAdminUserStatResponseBody:
    has_more: bool | None
    page_token: str | None
    items: list[AdminUserStat] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ListAdminUserStatResponseBodyBuilder: ...

class ListAdminUserStatResponseBodyBuilder:
    def __init__(self) -> None: ...
    def has_more(self, has_more: bool) -> ListAdminUserStatResponseBodyBuilder: ...
    def page_token(self, page_token: str) -> ListAdminUserStatResponseBodyBuilder: ...
    def items(self, items: list[AdminUserStat]) -> ListAdminUserStatResponseBodyBuilder: ...
    def build(self) -> ListAdminUserStatResponseBody: ...
