from lark_oapi.core.construct import init as init

class DatetimeSetting:
    format: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DatetimeSettingBuilder: ...

class DatetimeSettingBuilder:
    def __init__(self) -> None: ...
    def format(self, format: str) -> DatetimeSettingBuilder: ...
    def build(self) -> DatetimeSetting: ...
