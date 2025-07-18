from lark_oapi.core.construct import init as init

class AppliOfferBasicCustObjOpV:
    zh_cn: str | None
    en_us: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> AppliOfferBasicCustObjOpVBuilder: ...

class AppliOfferBasicCustObjOpVBuilder:
    def __init__(self) -> None: ...
    def zh_cn(self, zh_cn: str) -> AppliOfferBasicCustObjOpVBuilder: ...
    def en_us(self, en_us: str) -> AppliOfferBasicCustObjOpVBuilder: ...
    def build(self) -> AppliOfferBasicCustObjOpV: ...
