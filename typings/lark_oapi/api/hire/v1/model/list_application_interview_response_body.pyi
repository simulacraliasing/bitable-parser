from .interview import Interview as Interview
from lark_oapi.core.construct import init as init

class ListApplicationInterviewResponseBody:
    page_token: str | None
    has_more: bool | None
    items: list[Interview] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ListApplicationInterviewResponseBodyBuilder: ...

class ListApplicationInterviewResponseBodyBuilder:
    def __init__(self) -> None: ...
    def page_token(self, page_token: str) -> ListApplicationInterviewResponseBodyBuilder: ...
    def has_more(self, has_more: bool) -> ListApplicationInterviewResponseBodyBuilder: ...
    def items(self, items: list[Interview]) -> ListApplicationInterviewResponseBodyBuilder: ...
    def build(self) -> ListApplicationInterviewResponseBody: ...
