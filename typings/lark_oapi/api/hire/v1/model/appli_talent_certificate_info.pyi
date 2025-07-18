from lark_oapi.core.construct import init as init

class AppliTalentCertificateInfo:
    id: str | None
    name: str | None
    desc: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> AppliTalentCertificateInfoBuilder: ...

class AppliTalentCertificateInfoBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> AppliTalentCertificateInfoBuilder: ...
    def name(self, name: str) -> AppliTalentCertificateInfoBuilder: ...
    def desc(self, desc: str) -> AppliTalentCertificateInfoBuilder: ...
    def build(self) -> AppliTalentCertificateInfo: ...
