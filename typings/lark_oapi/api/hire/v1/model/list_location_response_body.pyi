from .location import Location as Location
from lark_oapi.core.construct import init as init

class ListLocationResponseBody:
    items: list[Location] | None
    has_more: bool | None
    page_token: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ListLocationResponseBodyBuilder: ...

class ListLocationResponseBodyBuilder:
    def __init__(self) -> None: ...
    def items(self, items: list[Location]) -> ListLocationResponseBodyBuilder: ...
    def has_more(self, has_more: bool) -> ListLocationResponseBodyBuilder: ...
    def page_token(self, page_token: str) -> ListLocationResponseBodyBuilder: ...
    def build(self) -> ListLocationResponseBody: ...
