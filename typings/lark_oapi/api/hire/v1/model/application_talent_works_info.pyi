from lark_oapi.core.construct import init as init

class ApplicationTalentWorksInfo:
    id: str | None
    link: str | None
    desc: str | None
    name: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ApplicationTalentWorksInfoBuilder: ...

class ApplicationTalentWorksInfoBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> ApplicationTalentWorksInfoBuilder: ...
    def link(self, link: str) -> ApplicationTalentWorksInfoBuilder: ...
    def desc(self, desc: str) -> ApplicationTalentWorksInfoBuilder: ...
    def name(self, name: str) -> ApplicationTalentWorksInfoBuilder: ...
    def build(self) -> ApplicationTalentWorksInfo: ...
