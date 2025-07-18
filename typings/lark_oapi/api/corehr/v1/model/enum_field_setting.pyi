from .common_schema_option import CommonSchemaOption as CommonSchemaOption
from lark_oapi.core.construct import init as init

class EnumFieldSetting:
    enum_field_option_list: list[CommonSchemaOption] | None
    is_multiple: bool | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> EnumFieldSettingBuilder: ...

class EnumFieldSettingBuilder:
    def __init__(self) -> None: ...
    def enum_field_option_list(self, enum_field_option_list: list[CommonSchemaOption]) -> EnumFieldSettingBuilder: ...
    def is_multiple(self, is_multiple: bool) -> EnumFieldSettingBuilder: ...
    def build(self) -> EnumFieldSetting: ...
