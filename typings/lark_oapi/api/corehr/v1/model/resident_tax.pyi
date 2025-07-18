from .address import Address as Address
from .enum import Enum as Enum
from .object_field_data import ObjectFieldData as ObjectFieldData
from lark_oapi.core.construct import init as init

class ResidentTax:
    id: str | None
    year_resident_tax: str | None
    tax_address: Address | None
    tax_country_region_id: str | None
    resident_status: Enum | None
    resident_status_specification: str | None
    custom_fields: list[ObjectFieldData] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ResidentTaxBuilder: ...

class ResidentTaxBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> ResidentTaxBuilder: ...
    def year_resident_tax(self, year_resident_tax: str) -> ResidentTaxBuilder: ...
    def tax_address(self, tax_address: Address) -> ResidentTaxBuilder: ...
    def tax_country_region_id(self, tax_country_region_id: str) -> ResidentTaxBuilder: ...
    def resident_status(self, resident_status: Enum) -> ResidentTaxBuilder: ...
    def resident_status_specification(self, resident_status_specification: str) -> ResidentTaxBuilder: ...
    def custom_fields(self, custom_fields: list[ObjectFieldData]) -> ResidentTaxBuilder: ...
    def build(self) -> ResidentTax: ...
