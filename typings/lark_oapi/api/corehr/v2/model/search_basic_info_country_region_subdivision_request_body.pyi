from lark_oapi.core.construct import init as init

class SearchBasicInfoCountryRegionSubdivisionRequestBody:
    country_region_id_list: list[str] | None
    country_region_subdivision_id_list: list[str] | None
    status_list: list[int] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SearchBasicInfoCountryRegionSubdivisionRequestBodyBuilder: ...

class SearchBasicInfoCountryRegionSubdivisionRequestBodyBuilder:
    def __init__(self) -> None: ...
    def country_region_id_list(self, country_region_id_list: list[str]) -> SearchBasicInfoCountryRegionSubdivisionRequestBodyBuilder: ...
    def country_region_subdivision_id_list(self, country_region_subdivision_id_list: list[str]) -> SearchBasicInfoCountryRegionSubdivisionRequestBodyBuilder: ...
    def status_list(self, status_list: list[int]) -> SearchBasicInfoCountryRegionSubdivisionRequestBodyBuilder: ...
    def build(self) -> SearchBasicInfoCountryRegionSubdivisionRequestBody: ...
