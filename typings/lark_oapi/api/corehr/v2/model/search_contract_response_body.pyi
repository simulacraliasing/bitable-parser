from .contract import Contract as Contract
from lark_oapi.core.construct import init as init

class SearchContractResponseBody:
    items: list[Contract] | None
    page_token: str | None
    has_more: bool | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SearchContractResponseBodyBuilder: ...

class SearchContractResponseBodyBuilder:
    def __init__(self) -> None: ...
    def items(self, items: list[Contract]) -> SearchContractResponseBodyBuilder: ...
    def page_token(self, page_token: str) -> SearchContractResponseBodyBuilder: ...
    def has_more(self, has_more: bool) -> SearchContractResponseBodyBuilder: ...
    def build(self) -> SearchContractResponseBody: ...
