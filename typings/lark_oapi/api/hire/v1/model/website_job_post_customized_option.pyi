from .i18n import I18n as I18n
from lark_oapi.core.construct import init as init

class WebsiteJobPostCustomizedOption:
    key: str | None
    name: I18n | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> WebsiteJobPostCustomizedOptionBuilder: ...

class WebsiteJobPostCustomizedOptionBuilder:
    def __init__(self) -> None: ...
    def key(self, key: str) -> WebsiteJobPostCustomizedOptionBuilder: ...
    def name(self, name: I18n) -> WebsiteJobPostCustomizedOptionBuilder: ...
    def build(self) -> WebsiteJobPostCustomizedOption: ...
