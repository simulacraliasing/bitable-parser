from lark_oapi.core.construct import init as init

class ChatTabConfig:
    icon_key: str | None
    is_built_in: bool | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ChatTabConfigBuilder: ...

class ChatTabConfigBuilder:
    def __init__(self) -> None: ...
    def icon_key(self, icon_key: str) -> ChatTabConfigBuilder: ...
    def is_built_in(self, is_built_in: bool) -> ChatTabConfigBuilder: ...
    def build(self) -> ChatTabConfig: ...
