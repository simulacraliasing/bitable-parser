from .user_meta import UserMeta as UserMeta
from lark_oapi.core.construct import init as init

class SearchUserDataAi:
    query_keyword: str | None
    user_info: UserMeta | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SearchUserDataAiBuilder: ...

class SearchUserDataAiBuilder:
    def __init__(self) -> None: ...
    def query_keyword(self, query_keyword: str) -> SearchUserDataAiBuilder: ...
    def user_info(self, user_info: UserMeta) -> SearchUserDataAiBuilder: ...
    def build(self) -> SearchUserDataAi: ...
