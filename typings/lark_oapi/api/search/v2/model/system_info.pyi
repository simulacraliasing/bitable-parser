from lark_oapi.core.construct import init as init

class SystemInfo:
    time: str | None
    time_zone: str | None
    lang: str | None
    brand: str | None
    weekday: str | None
    session_id: str | None
    shadow_name: str | None
    msg_id: str | None
    agent_id: str | None
    locale: str | None
    app_version: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SystemInfoBuilder: ...

class SystemInfoBuilder:
    def __init__(self) -> None: ...
    def time(self, time: str) -> SystemInfoBuilder: ...
    def time_zone(self, time_zone: str) -> SystemInfoBuilder: ...
    def lang(self, lang: str) -> SystemInfoBuilder: ...
    def brand(self, brand: str) -> SystemInfoBuilder: ...
    def weekday(self, weekday: str) -> SystemInfoBuilder: ...
    def session_id(self, session_id: str) -> SystemInfoBuilder: ...
    def shadow_name(self, shadow_name: str) -> SystemInfoBuilder: ...
    def msg_id(self, msg_id: str) -> SystemInfoBuilder: ...
    def agent_id(self, agent_id: str) -> SystemInfoBuilder: ...
    def locale(self, locale: str) -> SystemInfoBuilder: ...
    def app_version(self, app_version: str) -> SystemInfoBuilder: ...
    def build(self) -> SystemInfo: ...
