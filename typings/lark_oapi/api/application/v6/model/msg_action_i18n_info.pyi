from lark_oapi.core.construct import init as init

class MsgActionI18nInfo:
    i18n_key: str | None
    name: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> MsgActionI18nInfoBuilder: ...

class MsgActionI18nInfoBuilder:
    def __init__(self) -> None: ...
    def i18n_key(self, i18n_key: str) -> MsgActionI18nInfoBuilder: ...
    def name(self, name: str) -> MsgActionI18nInfoBuilder: ...
    def build(self) -> MsgActionI18nInfo: ...
