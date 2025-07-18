from lark_oapi.core.construct import init as init

class RestrictedModeSetting:
    status: bool | None
    screenshot_has_permission_setting: str | None
    download_has_permission_setting: str | None
    message_has_permission_setting: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> RestrictedModeSettingBuilder: ...

class RestrictedModeSettingBuilder:
    def __init__(self) -> None: ...
    def status(self, status: bool) -> RestrictedModeSettingBuilder: ...
    def screenshot_has_permission_setting(self, screenshot_has_permission_setting: str) -> RestrictedModeSettingBuilder: ...
    def download_has_permission_setting(self, download_has_permission_setting: str) -> RestrictedModeSettingBuilder: ...
    def message_has_permission_setting(self, message_has_permission_setting: str) -> RestrictedModeSettingBuilder: ...
    def build(self) -> RestrictedModeSetting: ...
