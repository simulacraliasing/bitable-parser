from .department_tree import DepartmentTree as DepartmentTree
from lark_oapi.core.construct import init as init

class TreeDepartmentResponseBody:
    items: list[DepartmentTree] | None
    page_token: str | None
    has_more: bool | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> TreeDepartmentResponseBodyBuilder: ...

class TreeDepartmentResponseBodyBuilder:
    def __init__(self) -> None: ...
    def items(self, items: list[DepartmentTree]) -> TreeDepartmentResponseBodyBuilder: ...
    def page_token(self, page_token: str) -> TreeDepartmentResponseBodyBuilder: ...
    def has_more(self, has_more: bool) -> TreeDepartmentResponseBodyBuilder: ...
    def build(self) -> TreeDepartmentResponseBody: ...
