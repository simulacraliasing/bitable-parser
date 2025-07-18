from .datetime_setting import DatetimeSetting as DatetimeSetting
from .member import Member as Member
from .member_setting import MemberSetting as MemberSetting
from .number_setting import NumberSetting as NumberSetting
from .select_setting import SelectSetting as SelectSetting
from .text_setting import TextSetting as TextSetting
from lark_oapi.core.construct import init as init

class CustomField:
    guid: str | None
    name: str | None
    type: str | None
    number_setting: NumberSetting | None
    member_setting: MemberSetting | None
    datetime_setting: DatetimeSetting | None
    single_select_setting: SelectSetting | None
    multi_select_setting: SelectSetting | None
    creator: Member | None
    created_at: str | None
    updated_at: str | None
    text_setting: TextSetting | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CustomFieldBuilder: ...

class CustomFieldBuilder:
    def __init__(self) -> None: ...
    def guid(self, guid: str) -> CustomFieldBuilder: ...
    def name(self, name: str) -> CustomFieldBuilder: ...
    def type(self, type: str) -> CustomFieldBuilder: ...
    def number_setting(self, number_setting: NumberSetting) -> CustomFieldBuilder: ...
    def member_setting(self, member_setting: MemberSetting) -> CustomFieldBuilder: ...
    def datetime_setting(self, datetime_setting: DatetimeSetting) -> CustomFieldBuilder: ...
    def single_select_setting(self, single_select_setting: SelectSetting) -> CustomFieldBuilder: ...
    def multi_select_setting(self, multi_select_setting: SelectSetting) -> CustomFieldBuilder: ...
    def creator(self, creator: Member) -> CustomFieldBuilder: ...
    def created_at(self, created_at: str) -> CustomFieldBuilder: ...
    def updated_at(self, updated_at: str) -> CustomFieldBuilder: ...
    def text_setting(self, text_setting: TextSetting) -> CustomFieldBuilder: ...
    def build(self) -> CustomField: ...
