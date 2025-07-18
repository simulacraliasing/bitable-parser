from lark_oapi.core.construct import init as init

class ResumeCertificate:
    name: str | None
    desc: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ResumeCertificateBuilder: ...

class ResumeCertificateBuilder:
    def __init__(self) -> None: ...
    def name(self, name: str) -> ResumeCertificateBuilder: ...
    def desc(self, desc: str) -> ResumeCertificateBuilder: ...
    def build(self) -> ResumeCertificate: ...
