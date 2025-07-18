from .profile_setting_address import ProfileSettingAddress as ProfileSettingAddress
from .profile_setting_custom_field import ProfileSettingCustomField as ProfileSettingCustomField
from .profile_setting_phone import ProfileSettingPhone as ProfileSettingPhone
from lark_oapi.core.construct import init as init

class ProfileSettingEmergencyContact:
    legal_name: str | None
    relationship: str | None
    is_primary: bool | None
    phone: ProfileSettingPhone | None
    email: str | None
    address: ProfileSettingAddress | None
    custom_fields: list[ProfileSettingCustomField] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ProfileSettingEmergencyContactBuilder: ...

class ProfileSettingEmergencyContactBuilder:
    def __init__(self) -> None: ...
    def legal_name(self, legal_name: str) -> ProfileSettingEmergencyContactBuilder: ...
    def relationship(self, relationship: str) -> ProfileSettingEmergencyContactBuilder: ...
    def is_primary(self, is_primary: bool) -> ProfileSettingEmergencyContactBuilder: ...
    def phone(self, phone: ProfileSettingPhone) -> ProfileSettingEmergencyContactBuilder: ...
    def email(self, email: str) -> ProfileSettingEmergencyContactBuilder: ...
    def address(self, address: ProfileSettingAddress) -> ProfileSettingEmergencyContactBuilder: ...
    def custom_fields(self, custom_fields: list[ProfileSettingCustomField]) -> ProfileSettingEmergencyContactBuilder: ...
    def build(self) -> ProfileSettingEmergencyContact: ...
