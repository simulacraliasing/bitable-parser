from lark_oapi.core.construct import init as init

class ArchiveField:
    code: str | None
    title: str | None
    upper_titles: list[str] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ArchiveFieldBuilder: ...

class ArchiveFieldBuilder:
    def __init__(self) -> None: ...
    def code(self, code: str) -> ArchiveFieldBuilder: ...
    def title(self, title: str) -> ArchiveFieldBuilder: ...
    def upper_titles(self, upper_titles: list[str]) -> ArchiveFieldBuilder: ...
    def build(self) -> ArchiveField: ...
