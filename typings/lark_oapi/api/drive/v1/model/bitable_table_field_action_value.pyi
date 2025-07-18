from .bitable_table_field_action_value_property import BitableTableFieldActionValueProperty as BitableTableFieldActionValueProperty
from lark_oapi.core.construct import init as init

class BitableTableFieldActionValue:
    id: str | None
    name: str | None
    type: int | None
    description: str | None
    property: BitableTableFieldActionValueProperty | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> BitableTableFieldActionValueBuilder: ...

class BitableTableFieldActionValueBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> BitableTableFieldActionValueBuilder: ...
    def name(self, name: str) -> BitableTableFieldActionValueBuilder: ...
    def type(self, type: int) -> BitableTableFieldActionValueBuilder: ...
    def description(self, description: str) -> BitableTableFieldActionValueBuilder: ...
    def property(self, property: BitableTableFieldActionValueProperty) -> BitableTableFieldActionValueBuilder: ...
    def build(self) -> BitableTableFieldActionValue: ...
