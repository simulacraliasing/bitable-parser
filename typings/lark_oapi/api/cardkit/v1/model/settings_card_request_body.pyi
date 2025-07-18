from lark_oapi.core.construct import init as init

class SettingsCardRequestBody:
    settings: str | None
    uuid: str | None
    sequence: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SettingsCardRequestBodyBuilder: ...

class SettingsCardRequestBodyBuilder:
    def __init__(self) -> None: ...
    def settings(self, settings: str) -> SettingsCardRequestBodyBuilder: ...
    def uuid(self, uuid: str) -> SettingsCardRequestBodyBuilder: ...
    def sequence(self, sequence: int) -> SettingsCardRequestBodyBuilder: ...
    def build(self) -> SettingsCardRequestBody: ...
