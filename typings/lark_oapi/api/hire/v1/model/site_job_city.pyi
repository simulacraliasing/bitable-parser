from .site_name import SiteName as SiteName
from lark_oapi.core.construct import init as init

class SiteJobCity:
    city_code: str | None
    name: SiteName | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SiteJobCityBuilder: ...

class SiteJobCityBuilder:
    def __init__(self) -> None: ...
    def city_code(self, city_code: str) -> SiteJobCityBuilder: ...
    def name(self, name: SiteName) -> SiteJobCityBuilder: ...
    def build(self) -> SiteJobCity: ...
