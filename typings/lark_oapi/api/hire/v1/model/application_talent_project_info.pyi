from lark_oapi.core.construct import init as init

class ApplicationTalentProjectInfo:
    id: str | None
    name: str | None
    role: str | None
    link: str | None
    desc: str | None
    start_time: int | None
    end_time: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ApplicationTalentProjectInfoBuilder: ...

class ApplicationTalentProjectInfoBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> ApplicationTalentProjectInfoBuilder: ...
    def name(self, name: str) -> ApplicationTalentProjectInfoBuilder: ...
    def role(self, role: str) -> ApplicationTalentProjectInfoBuilder: ...
    def link(self, link: str) -> ApplicationTalentProjectInfoBuilder: ...
    def desc(self, desc: str) -> ApplicationTalentProjectInfoBuilder: ...
    def start_time(self, start_time: int) -> ApplicationTalentProjectInfoBuilder: ...
    def end_time(self, end_time: int) -> ApplicationTalentProjectInfoBuilder: ...
    def build(self) -> ApplicationTalentProjectInfo: ...
