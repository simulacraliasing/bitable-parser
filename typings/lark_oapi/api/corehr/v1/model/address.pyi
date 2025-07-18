from .enum import Enum as Enum
from .object_field_data import ObjectFieldData as ObjectFieldData
from lark_oapi.core.construct import init as init

class Address:
    full_address_local_script: str | None
    full_address_western_script: str | None
    id: str | None
    country_region_id: str | None
    region_id: str | None
    city_id: str | None
    distinct_id: str | None
    city_id_v2: str | None
    district_id_v2: str | None
    address_line1: str | None
    address_line2: str | None
    address_line3: str | None
    address_line4: str | None
    address_line5: str | None
    address_line6: str | None
    address_line7: str | None
    address_line8: str | None
    address_line9: str | None
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
    address_type_list: list[Enum] | None
    is_primary: bool | None
    is_public: bool | None
    custom_fields: list[ObjectFieldData] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> AddressBuilder: ...

class AddressBuilder:
    def __init__(self) -> None: ...
    def full_address_local_script(self, full_address_local_script: str) -> AddressBuilder: ...
    def full_address_western_script(self, full_address_western_script: str) -> AddressBuilder: ...
    def id(self, id: str) -> AddressBuilder: ...
    def country_region_id(self, country_region_id: str) -> AddressBuilder: ...
    def region_id(self, region_id: str) -> AddressBuilder: ...
    def city_id(self, city_id: str) -> AddressBuilder: ...
    def distinct_id(self, distinct_id: str) -> AddressBuilder: ...
    def city_id_v2(self, city_id_v2: str) -> AddressBuilder: ...
    def district_id_v2(self, district_id_v2: str) -> AddressBuilder: ...
    def address_line1(self, address_line1: str) -> AddressBuilder: ...
    def address_line2(self, address_line2: str) -> AddressBuilder: ...
    def address_line3(self, address_line3: str) -> AddressBuilder: ...
    def address_line4(self, address_line4: str) -> AddressBuilder: ...
    def address_line5(self, address_line5: str) -> AddressBuilder: ...
    def address_line6(self, address_line6: str) -> AddressBuilder: ...
    def address_line7(self, address_line7: str) -> AddressBuilder: ...
    def address_line8(self, address_line8: str) -> AddressBuilder: ...
    def address_line9(self, address_line9: str) -> AddressBuilder: ...
    def local_address_line1(self, local_address_line1: str) -> AddressBuilder: ...
    def local_address_line2(self, local_address_line2: str) -> AddressBuilder: ...
    def local_address_line3(self, local_address_line3: str) -> AddressBuilder: ...
    def local_address_line4(self, local_address_line4: str) -> AddressBuilder: ...
    def local_address_line5(self, local_address_line5: str) -> AddressBuilder: ...
    def local_address_line6(self, local_address_line6: str) -> AddressBuilder: ...
    def local_address_line7(self, local_address_line7: str) -> AddressBuilder: ...
    def local_address_line8(self, local_address_line8: str) -> AddressBuilder: ...
    def local_address_line9(self, local_address_line9: str) -> AddressBuilder: ...
    def postal_code(self, postal_code: str) -> AddressBuilder: ...
    def address_type_list(self, address_type_list: list[Enum]) -> AddressBuilder: ...
    def is_primary(self, is_primary: bool) -> AddressBuilder: ...
    def is_public(self, is_public: bool) -> AddressBuilder: ...
    def custom_fields(self, custom_fields: list[ObjectFieldData]) -> AddressBuilder: ...
    def build(self) -> Address: ...
