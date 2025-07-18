from .allowed_edit_modes import AllowedEditModes as AllowedEditModes
from .app_field_property_auto_serial import AppFieldPropertyAutoSerial as AppFieldPropertyAutoSerial
from .app_field_property_location import AppFieldPropertyLocation as AppFieldPropertyLocation
from .app_table_field_property_lookup_filter import AppTableFieldPropertyLookupFilter as AppTableFieldPropertyLookupFilter
from .app_table_field_property_option import AppTableFieldPropertyOption as AppTableFieldPropertyOption
from .app_table_field_property_type import AppTableFieldPropertyType as AppTableFieldPropertyType
from .rating import Rating as Rating
from lark_oapi.core.construct import init as init

class AppTableFieldProperty:
    options: list[AppTableFieldPropertyOption] | None
    formatter: str | None
    date_formatter: str | None
    auto_fill: bool | None
    multiple: bool | None
    table_id: str | None
    table_name: str | None
    back_field_name: str | None
    auto_serial: AppFieldPropertyAutoSerial | None
    location: AppFieldPropertyLocation | None
    formula_expression: str | None
    allowed_edit_modes: AllowedEditModes | None
    min: float | None
    max: float | None
    range_customize: bool | None
    currency_code: str | None
    rating: Rating | None
    type: AppTableFieldPropertyType | None
    filter_info: AppTableFieldPropertyLookupFilter | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> AppTableFieldPropertyBuilder: ...

class AppTableFieldPropertyBuilder:
    def __init__(self) -> None: ...
    def options(self, options: list[AppTableFieldPropertyOption]) -> AppTableFieldPropertyBuilder: ...
    def formatter(self, formatter: str) -> AppTableFieldPropertyBuilder: ...
    def date_formatter(self, date_formatter: str) -> AppTableFieldPropertyBuilder: ...
    def auto_fill(self, auto_fill: bool) -> AppTableFieldPropertyBuilder: ...
    def multiple(self, multiple: bool) -> AppTableFieldPropertyBuilder: ...
    def table_id(self, table_id: str) -> AppTableFieldPropertyBuilder: ...
    def table_name(self, table_name: str) -> AppTableFieldPropertyBuilder: ...
    def back_field_name(self, back_field_name: str) -> AppTableFieldPropertyBuilder: ...
    def auto_serial(self, auto_serial: AppFieldPropertyAutoSerial) -> AppTableFieldPropertyBuilder: ...
    def location(self, location: AppFieldPropertyLocation) -> AppTableFieldPropertyBuilder: ...
    def formula_expression(self, formula_expression: str) -> AppTableFieldPropertyBuilder: ...
    def allowed_edit_modes(self, allowed_edit_modes: AllowedEditModes) -> AppTableFieldPropertyBuilder: ...
    def min(self, min: float) -> AppTableFieldPropertyBuilder: ...
    def max(self, max: float) -> AppTableFieldPropertyBuilder: ...
    def range_customize(self, range_customize: bool) -> AppTableFieldPropertyBuilder: ...
    def currency_code(self, currency_code: str) -> AppTableFieldPropertyBuilder: ...
    def rating(self, rating: Rating) -> AppTableFieldPropertyBuilder: ...
    def type(self, type: AppTableFieldPropertyType) -> AppTableFieldPropertyBuilder: ...
    def filter_info(self, filter_info: AppTableFieldPropertyLookupFilter) -> AppTableFieldPropertyBuilder: ...
    def build(self) -> AppTableFieldProperty: ...
