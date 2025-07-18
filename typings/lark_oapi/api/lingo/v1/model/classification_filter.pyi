from lark_oapi.core.construct import init as init

class ClassificationFilter:
    include: list[str] | None
    exclude: list[str] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ClassificationFilterBuilder: ...

class ClassificationFilterBuilder:
    def __init__(self) -> None: ...
    def include(self, include: list[str]) -> ClassificationFilterBuilder: ...
    def exclude(self, exclude: list[str]) -> ClassificationFilterBuilder: ...
    def build(self) -> ClassificationFilter: ...
