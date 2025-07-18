from .app_table import AppTable as AppTable
from lark_oapi.core.construct import init as init

class ListAppTableResponseBody:
    has_more: bool | None
    page_token: str | None
    total: int | None
    items: list[AppTable] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ListAppTableResponseBodyBuilder: ...

class ListAppTableResponseBodyBuilder:
    def __init__(self) -> None: ...
    def has_more(self, has_more: bool) -> ListAppTableResponseBodyBuilder: ...
    def page_token(self, page_token: str) -> ListAppTableResponseBodyBuilder: ...
    def total(self, total: int) -> ListAppTableResponseBodyBuilder: ...
    def items(self, items: list[AppTable]) -> ListAppTableResponseBodyBuilder: ...
    def build(self) -> ListAppTableResponseBody: ...
