from .group import Group as Group
from lark_oapi.core.construct import init as init

class SimplelistGroupResponseBody:
    grouplist: list[Group] | None
    page_token: str | None
    has_more: bool | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SimplelistGroupResponseBodyBuilder: ...

class SimplelistGroupResponseBodyBuilder:
    def __init__(self) -> None: ...
    def grouplist(self, grouplist: list[Group]) -> SimplelistGroupResponseBodyBuilder: ...
    def page_token(self, page_token: str) -> SimplelistGroupResponseBodyBuilder: ...
    def has_more(self, has_more: bool) -> SimplelistGroupResponseBodyBuilder: ...
    def build(self) -> SimplelistGroupResponseBody: ...
