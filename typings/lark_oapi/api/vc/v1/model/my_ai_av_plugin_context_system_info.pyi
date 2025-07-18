from lark_oapi.core.construct import init as init

class MyAiAvPluginContextSystemInfo:
    lang: str | None
    brand: str | None
    locale: str | None
    session_id: str | None
    app_version: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> MyAiAvPluginContextSystemInfoBuilder: ...

class MyAiAvPluginContextSystemInfoBuilder:
    def __init__(self) -> None: ...
    def lang(self, lang: str) -> MyAiAvPluginContextSystemInfoBuilder: ...
    def brand(self, brand: str) -> MyAiAvPluginContextSystemInfoBuilder: ...
    def locale(self, locale: str) -> MyAiAvPluginContextSystemInfoBuilder: ...
    def session_id(self, session_id: str) -> MyAiAvPluginContextSystemInfoBuilder: ...
    def app_version(self, app_version: str) -> MyAiAvPluginContextSystemInfoBuilder: ...
    def build(self) -> MyAiAvPluginContextSystemInfo: ...
