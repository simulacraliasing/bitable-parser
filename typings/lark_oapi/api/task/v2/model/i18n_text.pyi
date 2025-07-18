from lark_oapi.core.construct import init as init

class I18nText:
    en_us: str | None
    zh_cn: str | None
    zh_hk: str | None
    zh_tw: str | None
    ja_jp: str | None
    fr_fr: str | None
    it_it: str | None
    de_de: str | None
    ru_ru: str | None
    th_th: str | None
    es_es: str | None
    ko_kr: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> I18nTextBuilder: ...

class I18nTextBuilder:
    def __init__(self) -> None: ...
    def en_us(self, en_us: str) -> I18nTextBuilder: ...
    def zh_cn(self, zh_cn: str) -> I18nTextBuilder: ...
    def zh_hk(self, zh_hk: str) -> I18nTextBuilder: ...
    def zh_tw(self, zh_tw: str) -> I18nTextBuilder: ...
    def ja_jp(self, ja_jp: str) -> I18nTextBuilder: ...
    def fr_fr(self, fr_fr: str) -> I18nTextBuilder: ...
    def it_it(self, it_it: str) -> I18nTextBuilder: ...
    def de_de(self, de_de: str) -> I18nTextBuilder: ...
    def ru_ru(self, ru_ru: str) -> I18nTextBuilder: ...
    def th_th(self, th_th: str) -> I18nTextBuilder: ...
    def es_es(self, es_es: str) -> I18nTextBuilder: ...
    def ko_kr(self, ko_kr: str) -> I18nTextBuilder: ...
    def build(self) -> I18nText: ...
