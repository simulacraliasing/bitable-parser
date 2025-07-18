from .faq import Faq as Faq
from lark_oapi.core.construct import init as init

class SearchFaqResponseBody:
    has_more: bool | None
    page_token: str | None
    items: list[Faq] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SearchFaqResponseBodyBuilder: ...

class SearchFaqResponseBodyBuilder:
    def __init__(self) -> None: ...
    def has_more(self, has_more: bool) -> SearchFaqResponseBodyBuilder: ...
    def page_token(self, page_token: str) -> SearchFaqResponseBodyBuilder: ...
    def items(self, items: list[Faq]) -> SearchFaqResponseBodyBuilder: ...
    def build(self) -> SearchFaqResponseBody: ...
