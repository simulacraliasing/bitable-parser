from .user_setting import UserSetting as UserSetting
from lark_oapi.core.construct import init as init

class QueryUserSettingResponseBody:
    user_settings: list[UserSetting] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> QueryUserSettingResponseBodyBuilder: ...

class QueryUserSettingResponseBodyBuilder:
    def __init__(self) -> None: ...
    def user_settings(self, user_settings: list[UserSetting]) -> QueryUserSettingResponseBodyBuilder: ...
    def build(self) -> QueryUserSettingResponseBody: ...
