from .profile_setting_file import ProfileSettingFile as ProfileSettingFile
from lark_oapi.core.construct import init as init

class ProfileSettingPersonalRecord:
    profile_type: str | None
    files: list[ProfileSettingFile] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ProfileSettingPersonalRecordBuilder: ...

class ProfileSettingPersonalRecordBuilder:
    def __init__(self) -> None: ...
    def profile_type(self, profile_type: str) -> ProfileSettingPersonalRecordBuilder: ...
    def files(self, files: list[ProfileSettingFile]) -> ProfileSettingPersonalRecordBuilder: ...
    def build(self) -> ProfileSettingPersonalRecord: ...
