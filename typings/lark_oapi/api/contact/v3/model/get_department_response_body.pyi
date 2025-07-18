from .department import Department as Department
from lark_oapi.core.construct import init as init

class GetDepartmentResponseBody:
    department: Department | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> GetDepartmentResponseBodyBuilder: ...

class GetDepartmentResponseBodyBuilder:
    def __init__(self) -> None: ...
    def department(self, department: Department) -> GetDepartmentResponseBodyBuilder: ...
    def build(self) -> GetDepartmentResponseBody: ...
