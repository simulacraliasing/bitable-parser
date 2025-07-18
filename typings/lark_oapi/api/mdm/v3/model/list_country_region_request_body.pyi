from .common import Common as Common
from .filter import Filter as Filter
from lark_oapi.core.construct import init as init

class ListCountryRegionRequestBody:
    filter: Filter | None
    common: Common | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ListCountryRegionRequestBodyBuilder: ...

class ListCountryRegionRequestBodyBuilder:
    def __init__(self) -> None: ...
    def filter(self, filter: Filter) -> ListCountryRegionRequestBodyBuilder: ...
    def common(self, common: Common) -> ListCountryRegionRequestBodyBuilder: ...
    def build(self) -> ListCountryRegionRequestBody: ...
