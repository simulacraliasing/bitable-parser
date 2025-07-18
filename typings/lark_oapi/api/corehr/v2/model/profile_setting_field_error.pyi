from lark_oapi.core.construct import init as init

class ProfileSettingFieldError:
    field_name: str | None
    error_msg: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ProfileSettingFieldErrorBuilder: ...

class ProfileSettingFieldErrorBuilder:
    def __init__(self) -> None: ...
    def field_name(self, field_name: str) -> ProfileSettingFieldErrorBuilder: ...
    def error_msg(self, error_msg: str) -> ProfileSettingFieldErrorBuilder: ...
    def build(self) -> ProfileSettingFieldError: ...
