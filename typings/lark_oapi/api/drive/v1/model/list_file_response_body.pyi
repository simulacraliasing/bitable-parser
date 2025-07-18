from .file import File as File
from lark_oapi.core.construct import init as init

class ListFileResponseBody:
    files: list[File] | None
    next_page_token: str | None
    has_more: bool | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ListFileResponseBodyBuilder: ...

class ListFileResponseBodyBuilder:
    def __init__(self) -> None: ...
    def files(self, files: list[File]) -> ListFileResponseBodyBuilder: ...
    def next_page_token(self, next_page_token: str) -> ListFileResponseBodyBuilder: ...
    def has_more(self, has_more: bool) -> ListFileResponseBodyBuilder: ...
    def build(self) -> ListFileResponseBody: ...
