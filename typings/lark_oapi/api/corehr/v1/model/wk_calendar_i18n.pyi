from lark_oapi.core.construct import init as init

class WkCalendarI18n:
    zh_cn: str | None
    en_us: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> WkCalendarI18nBuilder: ...

class WkCalendarI18nBuilder:
    def __init__(self) -> None: ...
    def zh_cn(self, zh_cn: str) -> WkCalendarI18nBuilder: ...
    def en_us(self, en_us: str) -> WkCalendarI18nBuilder: ...
    def build(self) -> WkCalendarI18n: ...
