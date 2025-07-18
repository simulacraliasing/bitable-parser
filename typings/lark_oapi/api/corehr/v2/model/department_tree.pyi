from lark_oapi.core.construct import init as init

class DepartmentTree:
    id: str | None
    level: int | None
    children: list[str] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DepartmentTreeBuilder: ...

class DepartmentTreeBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> DepartmentTreeBuilder: ...
    def level(self, level: int) -> DepartmentTreeBuilder: ...
    def children(self, children: list[str]) -> DepartmentTreeBuilder: ...
    def build(self) -> DepartmentTree: ...
