from .department_parents import DepartmentParents as DepartmentParents
from lark_oapi.core.construct import init as init

class ParentsDepartmentResponseBody:
    items: list[DepartmentParents] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ParentsDepartmentResponseBodyBuilder: ...

class ParentsDepartmentResponseBodyBuilder:
    def __init__(self) -> None: ...
    def items(self, items: list[DepartmentParents]) -> ParentsDepartmentResponseBodyBuilder: ...
    def build(self) -> ParentsDepartmentResponseBody: ...
