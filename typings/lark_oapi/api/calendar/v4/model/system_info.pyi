from lark_oapi.core.construct import init as init

class SystemInfo:
    session_id: str | None
    lang: str | None
    locale: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SystemInfoBuilder: ...

class SystemInfoBuilder:
    def __init__(self) -> None: ...
    def session_id(self, session_id: str) -> SystemInfoBuilder: ...
    def lang(self, lang: str) -> SystemInfoBuilder: ...
    def locale(self, locale: str) -> SystemInfoBuilder: ...
    def build(self) -> SystemInfo: ...
