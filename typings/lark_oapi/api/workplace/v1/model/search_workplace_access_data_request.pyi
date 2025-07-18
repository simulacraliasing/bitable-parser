from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class SearchWorkplaceAccessDataRequest(BaseRequest):
    from_date: str | None
    to_date: str | None
    page_size: int | None
    page_token: str | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> SearchWorkplaceAccessDataRequestBuilder: ...

class SearchWorkplaceAccessDataRequestBuilder:
    def __init__(self) -> None: ...
    def from_date(self, from_date: str) -> SearchWorkplaceAccessDataRequestBuilder: ...
    def to_date(self, to_date: str) -> SearchWorkplaceAccessDataRequestBuilder: ...
    def page_size(self, page_size: int) -> SearchWorkplaceAccessDataRequestBuilder: ...
    def page_token(self, page_token: str) -> SearchWorkplaceAccessDataRequestBuilder: ...
    def build(self) -> SearchWorkplaceAccessDataRequest: ...
