from .country_region import CountryRegion as CountryRegion
from lark_oapi.core.construct import init as init

class ListCountryRegionResponseBody:
    data: list[CountryRegion] | None
    total: str | None
    next_page_token: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ListCountryRegionResponseBodyBuilder: ...

class ListCountryRegionResponseBodyBuilder:
    def __init__(self) -> None: ...
    def data(self, data: list[CountryRegion]) -> ListCountryRegionResponseBodyBuilder: ...
    def total(self, total: str) -> ListCountryRegionResponseBodyBuilder: ...
    def next_page_token(self, next_page_token: str) -> ListCountryRegionResponseBodyBuilder: ...
    def build(self) -> ListCountryRegionResponseBody: ...
