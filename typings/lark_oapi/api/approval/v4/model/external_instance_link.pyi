from lark_oapi.core.construct import init as init

class ExternalInstanceLink:
    pc_link: str | None
    mobile_link: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ExternalInstanceLinkBuilder: ...

class ExternalInstanceLinkBuilder:
    def __init__(self) -> None: ...
    def pc_link(self, pc_link: str) -> ExternalInstanceLinkBuilder: ...
    def mobile_link(self, mobile_link: str) -> ExternalInstanceLinkBuilder: ...
    def build(self) -> ExternalInstanceLink: ...
