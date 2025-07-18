from .workplace_access_data import WorkplaceAccessData as WorkplaceAccessData
from lark_oapi.core.construct import init as init

class SearchWorkplaceAccessDataResponseBody:
    items: list[WorkplaceAccessData] | None
    has_more: bool | None
    page_token: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SearchWorkplaceAccessDataResponseBodyBuilder: ...

class SearchWorkplaceAccessDataResponseBodyBuilder:
    def __init__(self) -> None: ...
    def items(self, items: list[WorkplaceAccessData]) -> SearchWorkplaceAccessDataResponseBodyBuilder: ...
    def has_more(self, has_more: bool) -> SearchWorkplaceAccessDataResponseBodyBuilder: ...
    def page_token(self, page_token: str) -> SearchWorkplaceAccessDataResponseBodyBuilder: ...
    def build(self) -> SearchWorkplaceAccessDataResponseBody: ...
