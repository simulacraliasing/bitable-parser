from .enum import Enum as Enum
from lark_oapi.core.construct import init as init

class LocationAddressUpdate:
    country_region_id: str | None
    region_id: str | None
    city_id: str | None
    distinct_id: str | None
    local_address_line1: str | None
    local_address_line2: str | None
    local_address_line3: str | None
    local_address_line4: str | None
    local_address_line5: str | None
    local_address_line6: str | None
    local_address_line7: str | None
    local_address_line8: str | None
    local_address_line9: str | None
    postal_code: str | None
    address_types: list[Enum] | None
    is_primary: bool | None
    is_public: bool | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> LocationAddressUpdateBuilder: ...

class LocationAddressUpdateBuilder:
    def __init__(self) -> None: ...
    def country_region_id(self, country_region_id: str) -> LocationAddressUpdateBuilder: ...
    def region_id(self, region_id: str) -> LocationAddressUpdateBuilder: ...
    def city_id(self, city_id: str) -> LocationAddressUpdateBuilder: ...
    def distinct_id(self, distinct_id: str) -> LocationAddressUpdateBuilder: ...
    def local_address_line1(self, local_address_line1: str) -> LocationAddressUpdateBuilder: ...
    def local_address_line2(self, local_address_line2: str) -> LocationAddressUpdateBuilder: ...
    def local_address_line3(self, local_address_line3: str) -> LocationAddressUpdateBuilder: ...
    def local_address_line4(self, local_address_line4: str) -> LocationAddressUpdateBuilder: ...
    def local_address_line5(self, local_address_line5: str) -> LocationAddressUpdateBuilder: ...
    def local_address_line6(self, local_address_line6: str) -> LocationAddressUpdateBuilder: ...
    def local_address_line7(self, local_address_line7: str) -> LocationAddressUpdateBuilder: ...
    def local_address_line8(self, local_address_line8: str) -> LocationAddressUpdateBuilder: ...
    def local_address_line9(self, local_address_line9: str) -> LocationAddressUpdateBuilder: ...
    def postal_code(self, postal_code: str) -> LocationAddressUpdateBuilder: ...
    def address_types(self, address_types: list[Enum]) -> LocationAddressUpdateBuilder: ...
    def is_primary(self, is_primary: bool) -> LocationAddressUpdateBuilder: ...
    def is_public(self, is_public: bool) -> LocationAddressUpdateBuilder: ...
    def build(self) -> LocationAddressUpdate: ...
