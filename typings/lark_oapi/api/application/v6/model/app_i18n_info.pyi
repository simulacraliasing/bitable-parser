from lark_oapi.core.construct import init as init

class AppI18nInfo:
    i18n_key: str | None
    name: str | None
    description: str | None
    help_use: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> AppI18nInfoBuilder: ...

class AppI18nInfoBuilder:
    def __init__(self) -> None: ...
    def i18n_key(self, i18n_key: str) -> AppI18nInfoBuilder: ...
    def name(self, name: str) -> AppI18nInfoBuilder: ...
    def description(self, description: str) -> AppI18nInfoBuilder: ...
    def help_use(self, help_use: str) -> AppI18nInfoBuilder: ...
    def build(self) -> AppI18nInfo: ...
