from lark_oapi.core.construct import init as init

class LateOffLateOnSetting:
    late_off_base_on_time_type: int | None
    late_on_base_on_time_type: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> LateOffLateOnSettingBuilder: ...

class LateOffLateOnSettingBuilder:
    def __init__(self) -> None: ...
    def late_off_base_on_time_type(self, late_off_base_on_time_type: int) -> LateOffLateOnSettingBuilder: ...
    def late_on_base_on_time_type(self, late_on_base_on_time_type: int) -> LateOffLateOnSettingBuilder: ...
    def build(self) -> LateOffLateOnSetting: ...
