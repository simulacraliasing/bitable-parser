from .subregion import Subregion as Subregion
from lark_oapi.core.construct import init as init

class ListSubregionResponseBody:
    items: list[Subregion] | None
    has_more: bool | None
    page_token: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ListSubregionResponseBodyBuilder: ...

class ListSubregionResponseBodyBuilder:
    def __init__(self) -> None: ...
    def items(self, items: list[Subregion]) -> ListSubregionResponseBodyBuilder: ...
    def has_more(self, has_more: bool) -> ListSubregionResponseBodyBuilder: ...
    def page_token(self, page_token: str) -> ListSubregionResponseBodyBuilder: ...
    def build(self) -> ListSubregionResponseBody: ...
