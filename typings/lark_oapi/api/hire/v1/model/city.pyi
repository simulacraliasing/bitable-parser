from .country import Country as Country
from lark_oapi.core.construct import init as init

class City:
    city_code: str | None
    name: str | None
    en_name: str | None
    country: Country | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CityBuilder: ...

class CityBuilder:
    def __init__(self) -> None: ...
    def city_code(self, city_code: str) -> CityBuilder: ...
    def name(self, name: str) -> CityBuilder: ...
    def en_name(self, en_name: str) -> CityBuilder: ...
    def country(self, country: Country) -> CityBuilder: ...
    def build(self) -> City: ...
