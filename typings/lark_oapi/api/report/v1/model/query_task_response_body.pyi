from .task import Task as Task
from lark_oapi.core.construct import init as init

class QueryTaskResponseBody:
    items: list[Task] | None
    has_more: bool | None
    page_token: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> QueryTaskResponseBodyBuilder: ...

class QueryTaskResponseBodyBuilder:
    def __init__(self) -> None: ...
    def items(self, items: list[Task]) -> QueryTaskResponseBodyBuilder: ...
    def has_more(self, has_more: bool) -> QueryTaskResponseBodyBuilder: ...
    def page_token(self, page_token: str) -> QueryTaskResponseBodyBuilder: ...
    def build(self) -> QueryTaskResponseBody: ...
