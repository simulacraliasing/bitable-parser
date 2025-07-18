from .job_change import JobChange as JobChange
from lark_oapi.core.construct import init as init

class SearchJobChangeResponseBody:
    items: list[JobChange] | None
    has_more: bool | None
    page_token: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SearchJobChangeResponseBodyBuilder: ...

class SearchJobChangeResponseBodyBuilder:
    def __init__(self) -> None: ...
    def items(self, items: list[JobChange]) -> SearchJobChangeResponseBodyBuilder: ...
    def has_more(self, has_more: bool) -> SearchJobChangeResponseBodyBuilder: ...
    def page_token(self, page_token: str) -> SearchJobChangeResponseBodyBuilder: ...
    def build(self) -> SearchJobChangeResponseBody: ...
