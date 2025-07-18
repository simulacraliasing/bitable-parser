from lark_oapi.core.construct import init as init

class AppAbilityWeb:
    enable: bool | None
    pc_url: str | None
    pc_new_page_open_mode: str | None
    mobile_url: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> AppAbilityWebBuilder: ...

class AppAbilityWebBuilder:
    def __init__(self) -> None: ...
    def enable(self, enable: bool) -> AppAbilityWebBuilder: ...
    def pc_url(self, pc_url: str) -> AppAbilityWebBuilder: ...
    def pc_new_page_open_mode(self, pc_new_page_open_mode: str) -> AppAbilityWebBuilder: ...
    def mobile_url(self, mobile_url: str) -> AppAbilityWebBuilder: ...
    def build(self) -> AppAbilityWeb: ...
