from .list_country_region_request_body import ListCountryRegionRequestBody as ListCountryRegionRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class ListCountryRegionRequest(BaseRequest):
    languages: list[str] | None
    fields: list[str] | None
    limit: int | None
    offset: int | None
    return_count: bool | None
    page_token: str | None
    request_body: ListCountryRegionRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> ListCountryRegionRequestBuilder: ...

class ListCountryRegionRequestBuilder:
    def __init__(self) -> None: ...
    def languages(self, languages: list[str]) -> ListCountryRegionRequestBuilder: ...
    def fields(self, fields: list[str]) -> ListCountryRegionRequestBuilder: ...
    def limit(self, limit: int) -> ListCountryRegionRequestBuilder: ...
    def offset(self, offset: int) -> ListCountryRegionRequestBuilder: ...
    def return_count(self, return_count: bool) -> ListCountryRegionRequestBuilder: ...
    def page_token(self, page_token: str) -> ListCountryRegionRequestBuilder: ...
    def request_body(self, request_body: ListCountryRegionRequestBody) -> ListCountryRegionRequestBuilder: ...
    def build(self) -> ListCountryRegionRequest: ...
