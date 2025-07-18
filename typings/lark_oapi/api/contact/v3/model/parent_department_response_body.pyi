from .department import Department as Department
from lark_oapi.core.construct import init as init

class ParentDepartmentResponseBody:
    has_more: bool | None
    page_token: str | None
    items: list[Department] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ParentDepartmentResponseBodyBuilder: ...

class ParentDepartmentResponseBodyBuilder:
    def __init__(self) -> None: ...
    def has_more(self, has_more: bool) -> ParentDepartmentResponseBodyBuilder: ...
    def page_token(self, page_token: str) -> ParentDepartmentResponseBodyBuilder: ...
    def items(self, items: list[Department]) -> ParentDepartmentResponseBodyBuilder: ...
    def build(self) -> ParentDepartmentResponseBody: ...
